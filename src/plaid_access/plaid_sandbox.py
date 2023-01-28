
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest


def get_sandbox_public_token(client, institution_id):
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=institution_id,
        initial_products=[Products('transactions')]
    )
    pt_response = client.sandbox_public_token_create(
        pt_request)

    return pt_response['public_token']
