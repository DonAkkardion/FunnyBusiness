import django
from django.db import models
from asyncio.windows_events import NULL
from email.policy import default
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User




class FB_user(User):

    balance = models.IntegerField('balance', default= '1000'),


