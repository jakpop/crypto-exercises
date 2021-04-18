import uvicorn
from fastapi import FastAPI

from src.web import symmetric
from src.web import asymmteric

app = FastAPI()

app.include_router(symmetric.router, prefix='/symmetric', tags=['symmetric'])
app.include_router(asymmteric.router, prefix='/asymmetric', tags=['asymmetric'])


# TODO jinja2

@app.get("/")
async def root():
    return {"message": "yoyo cryptography fastapi"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
