from fastapi import APIRouter

from src.model.Key import Key
from src.service.cryptography_service import CryptographyService

router = APIRouter()
cs = CryptographyService()


@router.get("/key")
async def get_key():
    return {"key": cs.get_symmetric_key()}


@router.post("/key")
async def post_key(key: Key):
    cs.set_symmetric_key(key)
    return key


@router.post("/encode")
async def encrypt_message(message: str) -> bytes:
    return cs.encrypt_symmetric(message)


@router.post("/decode")
async def decrypt_message(token: str) -> bytes:
    return cs.decrypt_symmetric(token.encode())

