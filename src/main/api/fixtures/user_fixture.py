import pytest

from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest



@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)


@pytest.fixture
def deposit_account_request(create_account, amount):
    return DepositAccountRequest(
        accountId=create_account.id,
        amount=amount
    )

@pytest.fixture
def create_two_accounts(api_manager, create_user_request):
    account_one = api_manager.user_steps.create_account(create_user_request)
    account_two = api_manager.user_steps.create_account(create_user_request)
    return account_one, account_two

@pytest.fixture
def deposit_first_account(api_manager, create_two_accounts, create_user_request):
    account_one, account_two = create_two_accounts
    deposit_request = DepositAccountRequest(
        accountId=account_one.id,
        amount=9000
    )
    api_manager.user_steps.deposit_account_valid(deposit_request, create_user_request)
    return account_one, account_two

@pytest.fixture
def transfer_account_request(deposit_first_account, amount):
    account_one, account_two = deposit_first_account
    return TransferAccountRequest(
        fromAccountId=account_one.id,
        toAccountId=account_two.id,
        amount=amount
    )

@pytest.fixture
def expected_transfer_balance(transfer_account_request):
    return 9000 - transfer_account_request.amount


@pytest.fixture
def create_user_credit_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user_credit(user_request)
    return user_request

@pytest.fixture
def create_credit_account(api_manager, create_user_credit_request):
    return api_manager.user_steps.create_account_credit(create_user_credit_request)

@pytest.fixture
def create_credit_request(create_credit_account, amount, term_months):
    return CreateCreditRequest(
        accountId=create_credit_account.id,
        amount=amount,
        termMonths=term_months
    )

@pytest.fixture
def credit_repay_request(api_manager, create_credit_account, create_user_credit_request, amount):
    create_credit_request = CreateCreditRequest(
        accountId=create_credit_account.id,
        amount=amount,
        termMonths=12
    )

    credit_response = api_manager.user_steps.create_credit_valid(create_credit_request, create_user_credit_request)
    return CreditRepayRequest(
        creditId=credit_response.credit_id,
        accountId=create_credit_account.id,
        amount=amount
    )

@pytest.fixture
def credit_repay_invalid_request(api_manager, create_credit_account, create_user_credit_request, amount):
    create_credit_request = CreateCreditRequest(
        accountId=create_credit_account.id,
        amount=10000,
        termMonths=12
    )

    credit_response = api_manager.user_steps.create_credit_valid(create_credit_request, create_user_credit_request)
    return CreditRepayRequest(
        creditId=credit_response.credit_id,
        accountId=create_credit_account.id,
        amount=amount
    )