from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import *

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"variants", ProductVariantsViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("",include(router.urls)),
    path("docs/", include_docs_urls(title="Ecommerce API")),
]