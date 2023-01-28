from django.conf import settings
from plaid_access.models import PlaidItem
from plaid_access.plaid_sandbox import get_sandbox_public_token
from plaid_access.plaid_client import create_client
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode


def create_link_token(user):
    client = create_client()
    client_user_id = str(user.id)

    request = LinkTokenCreateRequest(
        products=[Products("auth")],
        client_name="Budgetting Plaid Test App",
        country_codes=[CountryCode('US')],
        language='en',
        user=LinkTokenCreateRequestUser(
            client_user_id=client_user_id
        )
    )
    response = client.link_token_create(request)

    return response.to_dict()


def exchange_public_access_token(user, public_token):
    client = create_client()
    public_token = public_token or get_sandbox_public_token(
        client, settings.SANDBOX_INSTITUTIONS[0])

    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )

    try:
        response = client.item_public_token_exchange(request)
        print(f"the response is {response}", flush=True)
    except Exception as e:
        raise

    # These values should be saved to a persistent database and
    # associated with the currently signed-in user
    access_token = response['access_token']
    print(f"access_token = {access_token}")

    try:
        PlaidItem.objects.create(
            user=user,
            access_token=access_token,
        )
    except Exception:
        raise

    return access_token
