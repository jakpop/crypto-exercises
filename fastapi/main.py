from fastapi import FastAPI

from src.routers import symmetric
from src.routers import asymmteric

app = FastAPI()

app.include_router(symmetric.router)
app.include_router(asymmteric.router)


@app.get("/")
async def root():
    return {"message": "yoyo cryptography fastapi"}
