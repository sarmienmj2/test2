from django.db import models
from django.contrib.auth.models import AbstractUser
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
class Product(models.Model):
    STATUS_OPTIONS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    principalImage = models.URLField(max_length=200)
    imagesQuantity = models.IntegerField(blank=True, null=True)
    hasVariants = models.BooleanField(blank=True, null=True)
    variantType = models.CharField(max_length=100, blank=True, null=True)
    variantQuantity = models.IntegerField(blank=True, null=True)
    status = models.ChoicesField(choices=STATUS_OPTIONS, default='Activo', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(max_length=1000)
    image_url = models.URLField(max_length=1000)
    product = models.ForeignKey(Product, related_name='images' , on_delete=models.CASCADE)

class ProductVariants(models.Model):
    id = models.AutoField(primary_key=True)
    variant = models.CharField(max_length=100)
    quantity = models.IntegerField()
    cartItemId = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, related_name='variants' , on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email