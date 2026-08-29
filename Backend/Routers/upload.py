from fastapi.routing import APIRouter
from fastapi import File, UploadFile
import pandas as pd
from io import BytesIO
import sqlite3
from datetime import datetime, UTC

# connect to the database
def get_db_connection():
    return sqlite3.connect("products.db")

# normalize report columns
def normalize(col):
    col = (col.strip().lower()
           .replace(" ", "")
           .replace(",", "")
           .replace("_", "")
           .replace("-", "")
           .replace("#", "")
           .replace("*", ""))
    return col

# function for processing excel report
def process_excel(df):
    conn = get_db_connection()
    cursor = conn.cursor()

    # required columns
    required = {
        "itemnumber",
        "brandid",
        "itemdescription",
        "countryoforigin",
        "customername",
        "customernumber",
        "obligationnumber",
        "obligationdate",
        "pieces",
        "netsalesext$"
    }

    # check if all required columns exist
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


    for index, row in df.iterrows():

        product_id = row["itemnumber"]
        brand = row["brandid"]
        item_description = row["itemdescription"]
        country_of_origin = row["countryoforigin"]

        # derived fields
        domestic_status, has_multiple_countries = determine_country(country_of_origin)

        # preserve a_la_carte and manual override selections if they exist
        cursor.execute("SELECT is_a_la_carte, manual_override_status FROM products WHERE product_id = ?", (product_id,))
        existing = cursor.fetchone()

        if existing and existing[1] != "":
            is_a_la_carte = existing[0]
            manual_override_status = existing[1]
        else:
            is_a_la_carte = 0
            manual_override_status = ""

        # default exception flags
        exception_cheaper = 0
        exception_non_domestic = 0

        # notes start empty
        notes = ""

        timestamp = datetime.now(UTC).isoformat()

        # insert or replace data into products table
        cursor.execute("""INSERT or REPLACE INTO products (
                       product_id,
                       brand,
                       item_description,
                       country_of_origin,
                       domestic_status,
                       has_multiple_countries,
                       is_a_la_carte,
                       exception_cheaper,
                       exception_non_domestic,
                       manual_override_status,
                       last_updated,
                       notes
                       )
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""" ,
                       (
                           product_id,
                           brand,
                           item_description,
                           country_of_origin,
                           domestic_status,
                           has_multiple_countries,
                           is_a_la_carte,
                           exception_cheaper,
                           exception_non_domestic,
                           manual_override_status,
                           timestamp,
                           notes
                       ))

        # spending rows table data
        product_id_fk = product_id
        customer_name = row["customername"]
        customer_id = row["customernumber"]
        obligation_number = row["obligationnumber"]
        obligation_date = str(row["obligationdate"])
        quantity = row["pieces"]
        net_sales_ext = row["netsalesext$"]
        notes_2 = ""

        # insert or replace data for spending rows table
        cursor.execute("""INSERT or REPLACE INTO spending_rows (
                               product_id,
                               customer_name,
                               customer_id,
                               obligation_number,
                               obligation_date,
                               quantity,
                               net_sales_ext,
                               notes
                               )
                               VALUES (?,?,?,?,?,?,?,?)""",
                       (
                           product_id_fk,
                           customer_name,
                           customer_id,
                           obligation_number,
                           obligation_date,
                           quantity,
                           net_sales_ext,
                           notes_2
                       ))

    # commit changes
    conn.commit()
    conn.close()


def determine_country(country_of_origin):


    if pd.isna(country_of_origin):
        return "Unknown", 0

    # normalize countries
    parts = country_of_origin.split("|")
    countries = [c.strip().lower() for c in parts if c is not None and c.strip()]

    if not countries:
        return "Unknown", 0

    # check for multiple countries
    has_multiple_countries = 1 if len(set(countries)) > 1 else 0

    # check for domestic, foreign, or unknown status
    if all(c == "united states (the)" for c in countries):
        return "Domestic", has_multiple_countries
    if any(c == "unknown" for c in countries):
        return "Unknown", has_multiple_countries

    return "Foreign", has_multiple_countries

router = APIRouter()

@router.post("/upload")

# wait for file upload and process the excel file
async def upload(file: UploadFile = File(...)):
    raw_bytes = await file.read()
    buffer = BytesIO(raw_bytes)
    df = pd.read_excel(buffer)
    df.columns = [normalize(col) for col in df.columns]
    process_excel(df)



