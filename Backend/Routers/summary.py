from fastapi.routing import APIRouter
import sqlite3

router = APIRouter()

def get_db_connection():
    return sqlite3.connect(r"C:\Users\njdan\OneDrive\Buy_American_Project\Backend\Database\products.db")

@router.get("/summary")
def summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    product_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products WHERE domestic_status = 'Domestic'")
    domestic_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products WHERE domestic_status = 'Foreign'")
    foreign_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products WHERE domestic_status = 'Unknown'")
    unknown_count = cursor.fetchone()[0]

    cursor.execute("""SELECT SUM(net_sales_ext) FROM spending_rows s JOIN products p ON s.product_id = p.product_id
                      WHERE is_a_la_carte = 0""")
    total_spending = cursor.fetchone()[0]
    if total_spending is None:
        total_spending = 0

    cursor.execute("""SELECT SUM(net_sales_ext) FROM spending_rows s JOIN products p ON s.product_id = p.product_id 
                      WHERE p.domestic_status = 'Foreign' OR p.domestic_status = 'Unknown' AND p.is_a_la_carte = 0""")
    total_foreign = cursor.fetchone()[0]
    if total_foreign is None:
        total_foreign = 0

    cursor.execute("""SELECT SUM(net_sales_ext) FROM spending_rows s JOIN products p ON s.product_id = p.product_id
                      WHERE p.domestic_status = 'Domestic' AND p.is_a_la_carte = 0""")
    total_domestic = cursor.fetchone()[0]
    if total_domestic is None:
        total_domestic = 0

    if total_spending != 0:
        foreign_percentage = round((total_foreign / total_spending) * 100, 4)
        domestic_percentage = round((total_domestic / total_spending) * 100, 4)
    else:
        foreign_percentage = 0
        domestic_percentage = 0

    conn.close()

    return {
        "Products": {
            "Total": product_count,
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





