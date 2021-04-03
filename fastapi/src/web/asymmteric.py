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
    """
    Generates a pair of public and private keys
    :return: Public and private keys
    """
    return cs.get_asymmetric_key()


@router.get("/key/ssh")
async def get_key_ssh():
    """
    Generates a pair of public and private keys in ssh format
    :return: Public and private ssh keys
    """
    return cs.get_asymmetric_key_ssh()


@router.post("/key")
async def post_key(key: AsymmetricKey):
    """
    Sets a pair of public and private keys for asymmetric encryption on the server
    :param key: Keys to be set
    :return: the same keys passed in request
    """
    cs.set_asymmetric_keys(key)
    return key


@router.post("/sign")
async def sign_message(request: Message):
    """
    Signs a message with a private key
    :param request: Message to be signed
    :return: Signed message
    """
    return cs.sign_message(request.message)


@router.post("/verify")
async def verify_message(request: VerifyModel):
    """
    Verifies if the message was signed with a private key associated with given public key
    :param request: Signature and message to be verified
    """
    cs.verify_message(request.signature, request.message)


@router.post("/encode")
async def encrypt_message(request: Message) -> bytes:
    """
    Encrypts a message using asymmetric encryption
    :param request: Message to be encrypted
    :return: Encrypted message
    """
    return cs.encrypt_asymmetric(request.message)


@router.post("/decode")
async def decrypt_message(request: Message) -> bytes:
    """
    Decrypts a message using asymmetric encryption
    :param request: Encrypted message to be decrypted
    :return: Decrypted message
    """
    return cs.decrypt_asymmetric(request.message.encode())
