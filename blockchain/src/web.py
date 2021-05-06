from fastapi import APIRouter

from src.blockchain import Blockchain
from src.model import NewBlock, Transaction

router = APIRouter()
bc = Blockchain()

@router.get("/last-block")
async def get_last_block():
    return bc.last_block

@router.post("/new-block")
async def new_block(block: NewBlock):
    return bc.new_block(block.proof, block.previous_hash)

@router.post("/transaction")
async def new_transaction(transaction: Transaction):
    return bc.new_transaction(transaction.sender, transaction.recipient, transaction.amount)

