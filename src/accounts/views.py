from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from accounts.serializers import UserSerializer
from accounts.plaid_token import create_link_token

@api_view(['POST'])
def get_link_token(request):
    data = request.data
    username = data["username"] if "username" in data else None

    user = User.objects.get(username=username)
    try:
        token = create_link_token(user)
    except Exception as e:
        return HttpResponseBadRequest(f"There was an issue with token creation: {e}")
    return HttpResponse(f"Your token is {token}")


@api_view(['POST'])
def create_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    
    if not serializer.is_valid():
        return HttpResponseBadRequest(f"There was an issue: {serializer.errors}")
    
    try:
        user = User.objects.create(**data)
    except Exception as e:
        return HttpResponseBadRequest(f"Failure: {e}")

    return HttpResponse(f"Success! user \"{user}\" has been created.")

    

