from django.conf import settings
from django.db import models


class SearchHistoryPost(models.Model):

    departure_city = models.CharField(max_length=40, null=False)
    arrival_city = models.CharField(max_length=40, null=False)
    departure_date = models.DateField(null=False)
    arrival_date = models.DateField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
