from pydantic import BaseModel


class AsymmetricKey(BaseModel):
    public_key: str
    private_key: str
