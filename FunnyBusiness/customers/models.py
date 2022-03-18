from django.db import models
from asyncio.windows_events import NULL
from email.policy import default
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models




class FB_user(models.Model):

    username = models.CharField('username', default= 'admin', max_length= 50)
    firstname = models.CharField('firstname', default= 'ad', max_length= 50)
    lastname = models.CharField('lastname', default= 'min', max_length= 50)
    wallet = models.IntegerField('wallet', default= '1000')

    
    def __str__(self):
        return self.name

