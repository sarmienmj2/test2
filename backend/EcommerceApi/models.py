from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    principalImage = models.URLField(max_length=200)
    description = models.CharField(max_length=100)

class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.URLField(max_length=1000)
    product = models.ForeignKey(Product, related_name='images' , on_delete=models.CASCADE)

class ProductSizes(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=100)
    stock = models.IntegerField()
    cartItemId = models.CharField(max_length=100, unique=True)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    productId = models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(OrderItems)
    totalPrice = models.FloatField()
    itemsCount = models.IntegerField()
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    url = models.URLField( max_length=200, null=True, blank=True)
    logoUrl = models.CharField(max_length=100, null=True, blank=True)