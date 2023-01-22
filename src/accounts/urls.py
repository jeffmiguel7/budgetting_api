from django.urls import include, path, re_path
from rest_framework import routers

from accounts import views


urlpatterns = [
    path('token', views.get_link_token),
    path('user', views.create_user)
]
