from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField("user email",unique=True)
    #date_of_birth=models.DateField("user date of birth")
    
    #USERNAME_FIELD='email'