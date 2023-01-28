from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("access/", include('plaid_access.urls')),
    path("accounts/", include('accounts.urls'))
]
