from django.contrib import admin
from .models import Category, Products, Review, Raiting
from customers.models import FB_user


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Raiting)
admin.site.register(FB_user)

 