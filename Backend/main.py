from fastapi import FastAPI
from Routers.upload import router as upload_router
from Routers.summary import router as summary_router
from Routers.products import router as product_router
from Routers.reset import router as reset_router



app = FastAPI()
app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(product_router)
app.include_router(reset_router)
