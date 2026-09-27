from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.specs.requests_specs import RequestsSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def deposit_account_valid(self, deposit_account_request: DepositAccountRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response

    def deposit_account_invalid(self, deposit_account_request: DepositAccountRequest, create_user_request: CreateUserRequest):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_account_request)
        return response

    def transfer_account_valid(self, transfer_account_request: TransferAccountRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_account_request)
        return response

    def transfer_account_invalid(self, transfer_account_request: TransferAccountRequest, create_user_request: CreateUserRequest):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(transfer_account_request)
        return response

    def create_account_credit(self, create_user_credit_request: CreateUserCreditRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def create_credit_valid(self, create_credit_request: CreateCreditRequest, create_user_credit_request: CreateUserCreditRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_credit_request.username,
                                       password=create_user_credit_request.password),
            Endpoint.CREATE_CREDIT,
            ResponseSpecs.request_create()
        ).post(create_credit_request)
        return response

    def create_credit_invalid(self, create_credit_request: CreateCreditRequest, create_user_credit_request: CreateUserCreditRequest):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_credit_request.username,
                                       password=create_user_credit_request.password),
            Endpoint.CREATE_CREDIT,
            ResponseSpecs.request_bad()
        ).post(create_credit_request)
        return response

    def credit_repay_valid(self, credit_repay_request: CreditRepayRequest, create_user_credit_request: CreateUserCreditRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response

    def credit_repay_invalid(self, credit_repay_request: CreditRepayRequest, create_user_credit_request: CreateUserCreditRequest):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_unprocessable()
        ).post(credit_repay_request)
        return response