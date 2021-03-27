from fastapi import APIRouter

router = APIRouter()


@router.get("/key")
async def get_key():
    return None


@router.get("/key/ssh")
async def get_key_ssh():
    return None


@router.post("/key")
async def post_key():
    return None


@router.post("/verify")
async def verify_key():
    return None


@router.post("/sign")
async def sign_key():
    return None


@router.post("/encode")
async def encrypt_message(message: str):
    return message


@router.post("/decode")
async def decrypt_message(message: str):
    return message

