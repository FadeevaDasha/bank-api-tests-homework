import pytest

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
    def test_account_deposit_valid(self, amount, api_manager, create_user_request, deposit_account_request):
        response = api_manager.user_steps.deposit_account_valid(deposit_account_request, create_user_request)

        assert response.id == deposit_account_request.account_id
        assert response.balance == deposit_account_request.amount




    @pytest.mark.parametrize(
        "amount",
        [
            999.99,
            9001
        ]
    )
    def test_account_deposit_invalid(self, amount, api_manager, create_user_request, deposit_account_request):
        response = api_manager.user_steps.deposit_account_invalid(deposit_account_request, create_user_request)

        assert response.json()["error"] == "Amount must be between 1000 and 9000"
