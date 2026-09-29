from pydantic import Field
from src.main.api.models.base_model import BaseModel


class TransferAccountRequest(BaseModel):
    from_account_id: int = Field(alias='fromAccountId')
    to_account_id: int = Field(alias='toAccountId')
    amount: float