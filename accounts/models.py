from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField("user email",unique=True)
    
    USERNAME_FIELD='email'