from src.main.api.models.base_model import BaseModel
from pydantic import Field


class TransferAccountResponse(BaseModel):
    from_account_id: int = Field(alias='fromAccountId')
    to_account_id: int = Field(alias='toAccountId')
    from_account_id_balance: float = Field(alias='fromAccountIdBalance')