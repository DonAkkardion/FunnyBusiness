from django.contrib import admin
from .models import Category, Products, Review, Raiting


class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "img_tag", "isAvailable", "description", "requested","futureOwner"]

admin.site.register(Products, imageAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Raiting)


 