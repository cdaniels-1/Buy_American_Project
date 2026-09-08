from fastapi.routing import APIRouter
from Database.reset_db import *
from Routers.upload import get_db_path

router = APIRouter()

@router.post("/admin/reset-db")
def reset_db():
    db_path = get_db_path()
    delete_db(db_path)
    init_db(db_path)

    return {"status": "database reset"}



