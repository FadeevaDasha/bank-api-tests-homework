import pytest

@pytest.mark.api
class TestCreateCredit:
    @pytest.mark.parametrize(
    "amount, term_months",
    [
        (5000.0, 12),
        (15000, 12)
    ]
)
    def test_create_credit_valid(self, amount, term_months, api_manager, create_user_credit_request, create_credit_request):
        response = api_manager.user_steps.create_credit_valid(create_credit_request, create_user_credit_request)

        assert response.id == create_credit_request.account_id
        assert response.amount == create_credit_request.amount
        assert response.term_months == create_credit_request.term_months
        assert response.balance == create_credit_request.amount
        assert response.credit_id is not None


    @pytest.mark.parametrize(
        "amount, term_months",
        [
            (4999, 12),
            (16000, 12)
        ]
    )
    def test_create_credit_invalid(self, amount, term_months, api_manager, create_user_credit_request,
                                 create_credit_request):
        api_manager.user_steps.create_credit_invalid(create_credit_request, create_user_credit_request)
