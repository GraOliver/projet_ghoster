from django.db import models
from django.conf import settings

class Auteur(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
