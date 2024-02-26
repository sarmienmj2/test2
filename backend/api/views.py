from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    ordering = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('price', 'price'),
            ('category', 'category'),
            ('id', 'id')
        )
    )
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter

class ProductVariantsViewSet(viewsets.ModelViewSet):
    queryset = ProductVariants.objects.all()
    serializer_class = ProductVariantCreateSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer