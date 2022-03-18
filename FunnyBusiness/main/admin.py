from django.contrib import admin
from .models import Category, Products
from customers.models import FB_user


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(FB_user)

 