from fastapi import FastAPI
from Routers.upload import router as upload_router
from Routers.summary import router as summary_router
from Routers.override import router as override_router
from Routers.reset import router as reset_router
from Routers.products import router as product_router
from Routers.spending_rows import router as spending_rows_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(override_router)
app.include_router(reset_router)
app.include_router(product_router)
app.include_router(spending_rows_router)


