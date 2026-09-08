from fastapi import APIRouter
import sqlite3
from Routers.upload import get_db_path

router = APIRouter()

@router.get("/spending-rows")
def get_spending_rows():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spending_rows")
    rows = cursor.fetchall()
    conn.close()
    spending_rows = []

    for row in rows:
        (
            row_id,
            product_id,
            customer_name,
            customer_id,
            obligation_number,
            obligation_date,
            quantity,
            net_sales_ext,
            notes
        ) = row

        spending_rows.append({
            "row_id": row_id,
            "product_id": product_id,
            "customer_name": customer_name,
            "customer_id": customer_id,
            "obligation_number": obligation_number,
            "obligation_date": obligation_date,
            "quantity": quantity,
            "net_sales_ext": net_sales_ext,
            "notes": notes
        })

    return spending_rows
