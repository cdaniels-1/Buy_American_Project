from fastapi import FastAPI
from Routers.upload import router


app = FastAPI()
app.include_router(router)
