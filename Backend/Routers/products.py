from fastapi.routing import APIRouter
import sqlite3

router = APIRouter()

def get_db_connection():
    return sqlite3.connect(r"C:\Users\njdan\OneDrive\Buy_American_Project\Backend\Database\products.db")

@router.put("/products/{product_id}/a-la-carte")
def set_a_la_carte(product_id: int, is_a_la_carte: int ):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE products 
                      SET is_a_la_carte = ? 
                      WHERE product_id = ?""", (is_a_la_carte, product_id))

    conn.commit()
    conn.close()
    return {"status": "Success", "product_id": product_id, "is_a_la_carte": is_a_la_carte}

@router.put("/products/{product_id}/exception-cheaper")
def set_exception_cheaper(product_id: int, exception_cheaper: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE products
                      SET exception_cheaper = ?
                      WHERE product_id = ?""", (exception_cheaper, product_id))
    conn.commit()
    conn.close()
    return {"status": "Success", "product_id": product_id, "exception_cheaper": exception_cheaper}

@router.put("/products/{product_id}/exception-non-domestic")
def set_exception_non_domestic(product_id: int, exception_non_domestic: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE products
                      SET exception_non_domestic = ?
                      WHERE product_id = ?""", (exception_non_domestic, product_id))
    conn.commit()
    conn.close()
    return {"status": "Success", "product_id": product_id, "exception_non_domestic": exception_non_domestic}

