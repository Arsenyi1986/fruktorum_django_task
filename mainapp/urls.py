from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, LinkViewSet, ParsedDataViewSet

router = DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'links', LinkViewSet)
router.register(r'parsed-data', ParsedDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]