import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from  src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from sqlalchemy.orm import Session


@pytest.mark.api
class TestCreateCredit:
    @pytest.mark.parametrize(
    "amount, term_months",
    [
        (5000.0, 12),
        (15000, 12)
    ]
)
    def test_create_credit_valid(self, db_session: Session, amount: float, term_months: int, api_manager: ApiManager,
                                 create_user_credit_request: CreateUserCreditRequest, create_credit_request: CreditRepayRequest):
        response = api_manager.user_steps.create_credit_valid(create_credit_request, create_user_credit_request)

        assert response.id == create_credit_request.account_id
        assert response.amount == create_credit_request.amount
        assert response.term_months == create_credit_request.term_months
        assert response.balance == create_credit_request.amount
        assert response.credit_id is not None

        credit_from_db = Credit.get_credit_by_id(db_session, response.credit_id)

        assert credit_from_db.id == response.credit_id
        assert credit_from_db.amount == response.amount
        assert credit_from_db.term_months == response.term_months



    @pytest.mark.parametrize(
        "amount, term_months",
        [
            (4999, 12),
            (16000, 12)
        ]
    )
    def test_create_credit_invalid(self, db_session: Session, amount, term_months, api_manager, create_user_credit_request,
                                 create_credit_request):

         response = api_manager.user_steps.create_credit_invalid(create_credit_request, create_user_credit_request)

         assert response.json()["error"] == 'Amount must be between 5000 and 15000'

         credit_from_db = Credit.get_credit_by_id(db_session, create_credit_request.account_id)

         assert credit_from_db is None
