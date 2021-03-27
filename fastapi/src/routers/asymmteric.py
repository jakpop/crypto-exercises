from fastapi import APIRouter

router = APIRouter()


@router.get("/asymmetric/key/", tags=['asymmetric'])
async def get_key():
    return None


@router.get("/asymmetric/key/ssh", tags=['asymmetric'])
async def get_key_ssh():
    return None


@router.post("/asymmetric/key/", tags=['asymmetric'])
async def post_key():
    return None


@router.post("/asymmetric/verify/", tags=['asymmetric'])
async def verify_key():
    return None


@router.post("/asymmetric/sign/", tags=['asymmetric'])
async def sign_key():
    return None


@router.post("/asymmetric/encode/", tags=['asymmetric'])
async def encrypt_message(message: str):
    return None


@router.post("/asymmetric/decode/", tags=['asymmetric'])
async def decrypt_message(message: str):
    return None

