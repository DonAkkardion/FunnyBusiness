import django
from django.db import models
from email.policy import default
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    blockchainPublicKey = models.CharField(max_length=255, blank=True, null=True)




