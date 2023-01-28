import json

from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from plaid_access.helpers import get_user_from_request
from plaid_access.serializers import UserSerializer
from plaid_access.plaid_token import create_link_token
from plaid_access.plaid_token import exchange_public_access_token
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_user(request):
    data = request.data
    serializer = UserSerializer(data=data)

    if not serializer.is_valid():
        return HttpResponseBadRequest(f"Invalid request data for user creation: {serializer.errors}")

    try:
        user = User.objects.create(**data)
    except Exception as e:
        return HttpResponseBadRequest(f"User creation failed: {e}")

    return HttpResponse(f"Success! user \"{user}\" has been created.")


@api_view(['POST'])
def get_link_token(request):
    user = get_user_from_request(request)

    try:
        link_token = create_link_token(user)
    except Exception as e:
        return HttpResponseBadRequest(f"There was an issue with token creation: {e}")

    result = json.dumps(link_token, indent=4, sort_keys=True, default=str)
    return HttpResponse(result, content_type="application/json")


@api_view(['POST'])
def get_access_token(request):
    user = get_user_from_request(request)
    public_token = None

    if hasattr(request.data, "public_token"):
        public_token = getattr(request.data, "public_token")

    try:
        access_token = exchange_public_access_token(user, public_token)
    except Exception as e:
        return HttpResponseBadRequest(f"There was an issue with access token exchange: {e}")
    return HttpResponse(f"Your access token is {access_token}")
