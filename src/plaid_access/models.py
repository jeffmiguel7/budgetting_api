from django.db import models
from django.conf import settings

class PlaidItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=400, null=False)