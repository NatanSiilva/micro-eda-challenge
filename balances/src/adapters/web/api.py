from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.application.composer import BalancesRepositoryComposer

balances_router = APIRouter()


@balances_router.get("/balances/{account_id}")
async def get_balance(account_id: str):
    repository = BalancesRepositoryComposer.compose()
    balance = repository.get_by_account_id(account_id)

    balance = {
        "account_id": balance.account_id,
        "balance": balance.balance,
        "created_at": balance.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": balance.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return JSONResponse(content={"balance": balance})
