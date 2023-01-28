import plaid
from django.conf import settings
from plaid.api import plaid_api


def create_client():
    """
    Available environments are 'Production', 
    'Development', and 'Sandbox'.
    """
    host = (
        plaid.Environment.Production
        if settings.CURRENT_ENV == "production"
        else plaid.Environment.Sandbox
    )

    configuration = plaid.Configuration(
        host=host,
        api_key={
            'clientId': settings.PLAID_CLIENT_ID,
            'secret': settings.PLAID_SECRET,
        }
    )

    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    return client
