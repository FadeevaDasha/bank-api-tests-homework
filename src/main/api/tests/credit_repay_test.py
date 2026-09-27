import pytest

@pytest.mark.api
class TestCreditRepay:
    @pytest.mark.parametrize(
    'amount',
    [
        5000,
        15000
    ]
)
    def test_credit_repay_valid(self, amount, api_manager, create_user_credit_request, credit_repay_request):
        response = api_manager.user_steps.credit_repay_valid(credit_repay_request, create_user_credit_request)

        assert response.credit_id == credit_repay_request.credit_id
        assert response.amount_deposited == credit_repay_request.amount



    @pytest.mark.parametrize(
        'amount',
        [
            4999,
            14000
        ]
    )
    def test_credit_repay_invalid(self, amount, api_manager, create_user_credit_request, credit_repay_invalid_request):
        api_manager.user_steps.credit_repay_invalid(credit_repay_invalid_request, create_user_credit_request)
