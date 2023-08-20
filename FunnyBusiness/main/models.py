from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from Services.formatChecker import ContentTypeRestrictedFileField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe

class Category(models.Model):
    name = models.CharField('name', max_length= 10)
    
    def __str__(self):
        return self.name


class Raiting(models.Model):
    name = models.CharField('name', max_length= 10)
    
    def __str__(self):
        return self.name

class Review(models.Model):

    comments = models.TextField('comments', blank=False, max_length= 400)
    product_raiting = models.ForeignKey(Raiting, related_name="product_raiting" , on_delete= models.CASCADE)
    autor_raiting = models.ForeignKey(Raiting, related_name="autor_raiting" , on_delete= models.CASCADE)
    target = models.IntegerField("Review Target", blank=False)
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    

class Products(models.Model):

    name = models.CharField('name', max_length= 100)
    description = models.TextField('description', max_length= 400)
    price = models.PositiveIntegerField('price', validators=[MaxValueValidator(9999999999),MinValueValidator(1)])
    isAvailable = models.BooleanField(default=True)
    requested = models.BooleanField(default=False)            #New
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.IntegerField("Product Owner", blank=False)
    futureOwner = models.IntegerField("Future Product Owner", blank=True, null=True)  #New
    fileEntity = ContentTypeRestrictedFileField(
        null=False,
        blank=False, 
        upload_to="files/", 
        max_upload_size=1719664640,                                                #1719664640 = 2 gb#
        content_types=['*/*']
    )   
    # fileEntity = models.FileField(null=False, blank=False, upload_to="files/")
    fileEntityHashSSH256 = models.CharField('fileHash',default='default_value', max_length= 400, null=False, blank=False)


    def img_tag(self):
        return mark_safe('<img src="/../../media/%s" width="100" height="100" />' % (self.img))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


