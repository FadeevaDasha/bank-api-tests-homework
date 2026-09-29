import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from  src.main.api.db.crud.account_crud import AccountCrudDb as Account
from sqlalchemy.orm import Session


@pytest.mark.api
class TestAccountDeposit:
    @pytest.mark.parametrize(
        "amount",
        [
            1000.0,
            1000.5,
            5000.0,
            9000.0,
        ]
    )
    def test_account_deposit_valid(self, db_session: Session, amount: float, api_manager: ApiManager, create_user_request: CreateUserRequest,
                                   deposit_account_request: DepositAccountRequest):

        response = api_manager.user_steps.deposit_account_valid(deposit_account_request, create_user_request)

        assert response.id == deposit_account_request.account_id
        assert response.balance == deposit_account_request.amount

        account_from_db = Account.get_account_by_id(db_session, deposit_account_request.account_id)
        assert account_from_db.id == deposit_account_request.account_id
        assert account_from_db.balance == deposit_account_request.amount




    @pytest.mark.parametrize(
        "amount",
        [
            999.99,
            9001
        ]
    )
    def test_account_deposit_invalid(self,  db_session: Session, amount: float, api_manager: ApiManager, create_user_request: CreateUserRequest,
                                     deposit_account_request: DepositAccountRequest):

        response = api_manager.user_steps.deposit_account_invalid(deposit_account_request, create_user_request)

        assert response.json()["error"] == "Amount must be between 1000 and 9000"

        account_from_db = Account.get_account_by_id(db_session, deposit_account_request.account_id)

        assert account_from_db.id == deposit_account_request.account_id
        assert account_from_db.balance == 0.0
