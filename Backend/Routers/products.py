from fastapi.routing import APIRouter
from Routers.upload import get_db_path
from Routers.upload import determine_country
import sqlite3

router = APIRouter()

@router.get("/products")
def product_list():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        (
            product_id,
            brand,
            item_description,
            country_of_origin,
            domestic_status,
            has_multiple_countries,
            last_updated,
            director_country,
            is_a_la_carte,
            exception_cheaper,
            exception_non_domestic,
            manual_override_status,
            notes
        ) = row

        final_country = director_country if director_country else country_of_origin
        final_domestic_status, _ = determine_country(final_country)

        products.append({
            "product_id": product_id,
            "brand": brand,
            "item_description": item_description,

            # Final merged values
            "final_country": final_country,
            "final_domestic_status": final_domestic_status,

            # Sysco raw values
            "sysco_country": country_of_origin,
            "sysco_domestic_status": domestic_status,
            "has_multiple_countries": has_multiple_countries,

            # Director override raw values
            "override_country": director_country,
            "is_a_la_carte": is_a_la_carte,
            "exception_cheaper": exception_cheaper,
            "exception_non_domestic": exception_non_domestic,
            "manual_override_status": manual_override_status,
            "notes": notes
        })

    return products

@router.get("/products/{product_id}")
def product_details(product_id):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"error": "Product not found"}

    (
        product_id,
        brand,
        item_description,
        country_of_origin,
        domestic_status,
        has_multiple_countries,
        last_updated,
        director_country,
        is_a_la_carte,
        exception_cheaper,
        exception_non_domestic,
        manual_override_status,
        notes
    ) = row

    final_country = director_country if director_country else country_of_origin
    final_domestic_status, _ = determine_country(final_country)

    product = ({
        "product_id": product_id,
        "brand": brand,
        "item_description": item_description,

        # Final merged values
        "final_country": final_country,
        "final_domestic_status": final_domestic_status,

        # Sysco raw values
        "sysco_country": country_of_origin,
        "sysco_domestic_status": domestic_status,
        "has_multiple_countries": has_multiple_countries,

        # Director override raw values
        "override_country": director_country,
        "is_a_la_carte": is_a_la_carte,
        "exception_cheaper": exception_cheaper,
        "exception_non_domestic": exception_non_domestic,
        "manual_override_status": manual_override_status,
        "notes": notes
    })

    return product


