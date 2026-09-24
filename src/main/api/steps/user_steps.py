from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
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

    def deposit_account(self, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.unauth_headers(),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response