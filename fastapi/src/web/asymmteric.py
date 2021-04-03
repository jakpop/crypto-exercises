from fastapi import APIRouter

from src.model.asymmetric_key import AsymmetricKey
from src.model.key import Key
from src.model.message import Message
from src.model.verify_model import VerifyModel
from src.service.cryptography_service import CryptographyService

router = APIRouter()
cs = CryptographyService()


@router.get("/key")
async def get_key() -> dict:
    return cs.get_asymmetric_key()


@router.get("/key/ssh")
async def get_key_ssh():
    return cs.get_asymmetric_key_ssh()


@router.post("/key")
async def post_key(key: AsymmetricKey):
    cs.set_asymmetric_keys(key)
    return key


@router.post("/sign")
async def sign_message(request: Message):
    return cs.sign_message(request.message)


@router.post("/verify")
async def verify_message(request: VerifyModel):
    cs.verify_message(request.signature, request.message)


@router.post("/encode")
async def encrypt_message(request: Message) -> bytes:
    return cs.encrypt_asymmetric(request.message)


@router.post("/decode")
async def decrypt_message(request: Message) -> bytes:
    return cs.decrypt_asymmetric(request.message.encode())
