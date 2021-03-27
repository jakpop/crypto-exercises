from fastapi import APIRouter
from src.service.cryptography_service import CryptographyService

router = APIRouter()
cs = CryptographyService()


@router.get("/symmetric/key/", tags=['symmetric'])
async def get_key():
    return {"key": CryptographyService.get_key(cs)}


@router.post("/symmetric/key/", tags=['symmetric'])
async def post_key():
    return None


@router.post("/symmetric/encode/", tags=['symmetric'])
async def encrypt_message(message: str):
    return message


@router.post("/symmetric/decode/", tags=['symmetric'])
async def decrypt_message(message: str):
    return message

