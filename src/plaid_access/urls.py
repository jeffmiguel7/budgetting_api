from django.urls import path
from plaid_access import views


urlpatterns = [
    path('user', views.create_user),
    path('token', views.get_link_token),
    path('access_token', views.get_access_token)
]
