from fastapi import FastAPI

from src.routers import symmetric
from src.routers import asymmteric

app = FastAPI()

app.include_router(symmetric.router, prefix='/symmetric', tags=['symmetric'])
app.include_router(asymmteric.router, prefix='/asymmetric', tags=['asymmetric'])


@app.get("/")
async def root():
    return {"message": "yoyo cryptography fastapi"}
