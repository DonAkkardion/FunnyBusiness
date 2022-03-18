from asyncio.windows_events import NULL
from email.policy import default
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from customers.models import FB_user

class Category(models.Model):
    name = models.CharField('name', max_length= 10)
    
    def __str__(self):
        return self.name

class Products(models.Model):

    name = models.CharField('name', max_length= 100)
    description = models.TextField('description', max_length= 400)
    price = models.IntegerField('price')
    isAvailable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.IntegerField("Product Owner", blank=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


