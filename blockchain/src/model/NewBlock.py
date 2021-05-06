from pydantic import BaseModel


class Block(BaseModel):
    proof: float
    previous_hash: str