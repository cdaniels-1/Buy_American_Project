from fastapi.routing import APIRouter
from Routers.upload import get_db_path
import sqlite3
from Routers.products import determine_country  # import your merge logic

router = APIRouter()

@router.get("/summary")
def summary():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Counters
    total_products = 0
    domestic_count = 0
    foreign_count = 0
    unknown_count = 0

    total_spending = 0
    total_domestic = 0
    total_foreign = 0

    # Loop through products and recalc final domestic status
    for row in products:
        (
            product_id,
            brand,
            item_description,
            country_of_origin,
            domestic_status,          # Sysco
            has_multiple_countries,
            last_updated,
            director_country,         # Director override
            is_a_la_carte,
            exception_cheaper,
            exception_non_domestic,
            manual_override_status,
            notes
        ) = row

        # Skip a la carte entirely
        if is_a_la_carte == 1:
            continue

        # Recalculate final country using your override logic
        final_country = director_country if director_country else country_of_origin
        final_domestic_status, _ = determine_country(final_country)

        # Count products
        total_products += 1

        if final_domestic_status == "Domestic":
            domestic_count += 1
        elif final_domestic_status == "Foreign":
            foreign_count += 1
        else:
            unknown_count += 1

        # Spending rows for this product
        cursor.execute("""
            SELECT SUM(net_sales_ext)
            FROM spending_rows
            WHERE product_id = ?
        """, (product_id,))
        spending = cursor.fetchone()[0] or 0

        total_spending += spending

        if final_domestic_status == "Domestic":
            total_domestic += spending
        else:
            total_foreign += spending

    # Percentages
    if total_spending > 0:
        foreign_percentage = round((total_foreign / total_spending) * 100, 2)
        domestic_percentage = round((total_domestic / total_spending) * 100, 2)
    else:
        foreign_percentage = 0
        domestic_percentage = 0

    conn.close()

    return {
        "Products": {
            "Total": total_products,
            "Domestic": domestic_count,
            "Foreign": foreign_count,
            "Unknown": unknown_count,
        },
        "Spending": {
            "Total": total_spending,
            "Domestic": total_domestic,
            "Foreign": total_foreign,
            "Foreign percentage": foreign_percentage,
            "Domestic percentage": domestic_percentage,
        }
    }
