from rest_framework import serializers
from .models import *


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']
    
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'principalImage',
            'description',
            'images',
        ]
