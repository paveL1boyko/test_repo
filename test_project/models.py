from django.db import models


# Create your models here.

class FormData(models.Model):
    data = models.JSONField()
