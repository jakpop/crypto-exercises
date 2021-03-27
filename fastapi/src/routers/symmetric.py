from fastapi import APIRouter
from src.service.cryptography_service import CryptographyService

router = APIRouter()
cs = CryptographyService()


@router.get("/key")
async def get_key():
    return {"key": CryptographyService.get_key(cs)}


@router.post("/key")
async def post_key():
    return None


@router.post("/encode")
async def encrypt_message(message: str):
    return message


@router.post("/decode")
async def decrypt_message(message: str):
    return message

