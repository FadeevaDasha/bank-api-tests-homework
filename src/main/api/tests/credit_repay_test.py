import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from  src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from sqlalchemy.orm import Session


@pytest.mark.api
class TestCreditRepay:
    @pytest.mark.parametrize(
    'amount',
    [
        5000,
        15000
    ]
)
    def test_credit_repay_valid(self, db_session: Session, amount: float, api_manager: ApiManager, create_user_credit_request: CreateUserCreditRequest, credit_repay_request: CreditRepayRequest):

        response = api_manager.user_steps.credit_repay_valid(credit_repay_request, create_user_credit_request)

        assert response.credit_id == credit_repay_request.credit_id
        assert response.amount_deposited == credit_repay_request.amount

        credit_from_db = Credit.get_credit_by_id(db_session, credit_repay_request.credit_id)

        assert credit_from_db.id == credit_repay_request.credit_id
        assert credit_from_db.amount == credit_repay_request.amount



    @pytest.mark.parametrize(
        "amount, expected_error",
    [
        (4999, "The amount is not enough. Credit balance: -10000"),
        (14000, "Insufficient funds. Current balance: 10000.00, required: 14000.00"),
    ]
)
    def test_credit_repay_invalid(self, db_session: Session, amount: float, expected_error: str, api_manager: ApiManager,
                                  create_user_credit_request: CreateUserCreditRequest, credit_repay_invalid_request: CreditRepayRequest, credit_amount: float):

        response = api_manager.user_steps.credit_repay_invalid(credit_repay_invalid_request, create_user_credit_request)

        assert response.json()["error"] == expected_error

        credit_from_db = Credit.get_credit_by_id(db_session, credit_repay_invalid_request.credit_id)

        assert credit_from_db.id == credit_repay_invalid_request.credit_id
        assert credit_from_db.amount == credit_amount

