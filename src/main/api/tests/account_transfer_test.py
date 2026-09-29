import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from  src.main.api.db.crud.account_crud import AccountCrudDb as Account
from sqlalchemy.orm import Session


@pytest.mark.api
class TestAccountTransfer:
    @pytest.mark.parametrize(
        "amount",
        [
            500,
            5000
        ]
    )
    def test_account_transfer_valid(self, db_session: Session, amount: float, api_manager: ApiManager, create_user_request: CreateUserRequest,
                                    transfer_account_request: TransferAccountRequest, expected_transfer_balance: float):

        response = api_manager.user_steps.transfer_account_valid(transfer_account_request, create_user_request)

        assert response.from_account_id == transfer_account_request.from_account_id
        assert response.to_account_id == transfer_account_request.to_account_id
        assert response.from_account_id_balance == expected_transfer_balance

        account_one_db = Account.get_account_by_id(db_session, transfer_account_request.from_account_id)
        account_two_db = Account.get_account_by_id(db_session, transfer_account_request.to_account_id)

        assert account_one_db.id == transfer_account_request.from_account_id
        assert account_two_db.id == transfer_account_request.to_account_id

        assert account_one_db.balance == expected_transfer_balance
        assert account_two_db.balance == transfer_account_request.amount



    @pytest.mark.parametrize(
        "amount, expected_error",
        [
            (400, 'Amount must be between 500 and 10000'),
            (0, 'Amount must be greater than 0\nAmount must be between 500 and 10000')
        ]
    )
    def test_account_transfer_invalid(self, db_session: Session, amount: float, expected_error: str, api_manager: ApiManager, create_user_request: CreateUserRequest,
                                    transfer_account_request: TransferAccountRequest, transfer_initial_balance: float):

        response = api_manager.user_steps.transfer_account_invalid(transfer_account_request, create_user_request)

        assert response.json()["error"] == expected_error

        account_one_db = Account.get_account_by_id(db_session, transfer_account_request.from_account_id)
        account_two_db = Account.get_account_by_id(db_session, transfer_account_request.to_account_id)

        assert account_one_db.id == transfer_account_request.from_account_id
        assert account_two_db.id == transfer_account_request.to_account_id

        assert account_one_db.balance == transfer_initial_balance
        assert account_two_db.balance == 0
