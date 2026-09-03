from fastapi.routing import APIRouter
from Database.reset_db import *
router = APIRouter()

@router.post("/admin/reset-db")
def reset_db():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = str(os.path.dirname(current_dir))
    db_path = os.path.join(backend_dir, "Database", "products.db")

    delete_db(db_path)
    init_db(db_path)

    return {"status": "database reset"}



