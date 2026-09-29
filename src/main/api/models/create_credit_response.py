from src.main.api.models.base_model import BaseModel
from pydantic import Field


class CreateCreditResponse(BaseModel):
    id: int
    amount: float
    term_months: int = Field(alias='termMonths')
    balance: int
    credit_id: int = Field(alias='creditId')