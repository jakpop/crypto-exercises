from fastapi import APIRouter

from src.model.key import Key
from src.service.cryptography_service import CryptographyService

router = APIRouter()
cs = CryptographyService()


@router.get("/key")
async def get_key() -> dict[str, bytes]:
    """
    Generates a key with symmetric encryption
    :return: dict containing the key
    """
    return {"key": cs.get_symmetric_key()}


@router.post("/key")
async def post_key(key: Key) -> Key:
    """
    Sets a key for symmetric encryption on the server
    :param key: Key to be set
    :return: the same key passed in request
    """
    cs.set_symmetric_key(key)
    return key


@router.post("/encode")
async def encrypt_message(message: str) -> dict[str, bytes]:
    """
    Encrypts a message using symmetric encryption
    :param message: Message to be encrypted
    :return: Encrypted message
    """
    return {"message": cs.encrypt_symmetric(message)}


@router.post("/decode")
async def decrypt_message(token: str) -> dict[str, bytes]:
    """
    Decrypts a message using symmetric encryption
    :param token: Encrypted message to be decrypted
    :return: Decrypted message
    """
    return {"message": cs.decrypt_symmetric(token.encode())}

