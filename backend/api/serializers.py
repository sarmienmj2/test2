from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariants
        fields = ['id', 'size', 'stock', 'cartItemId']
class ProductVariantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariants
        fields = ['id', 'size', 'stock', 'cartItemId', 'product']
class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']
    
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True)
    variants = ProductVariantSerializer(many=True) 

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'principalImage',
            'description',
            'images',
            'variants',
            'category'
        ]
    
    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImages.objects.create(product=product, **image_data)
        return product
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user