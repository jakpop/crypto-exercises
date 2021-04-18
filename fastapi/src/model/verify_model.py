from pydantic import BaseModel


class VerifyModel(BaseModel):
    signature: str
    message: str
