import pytest

@pytest.mark.api
class TestAccountTransfer:
    @pytest.mark.parametrize(
        "amount",
        [
            500,
            5000
        ]
    )
    def test_account_transfer_valid(self, amount, api_manager, create_user_request, transfer_account_request,
                                    expected_transfer_balance):
        response = api_manager.user_steps.transfer_account_valid(transfer_account_request, create_user_request)

        assert response.from_account_id == transfer_account_request.from_account_id
        assert response.to_account_id == transfer_account_request.to_account_id
        assert response.from_account_id_balance == expected_transfer_balance

    @pytest.mark.parametrize(
        "amount",
        [
            400,
            0
        ]
    )
    def test_account_transfer_invalid(self, amount, api_manager, create_user_request, transfer_account_request):
        api_manager.user_steps.transfer_account_invalid(transfer_account_request, create_user_request)
