from django.urls import include, path
from rest_framework import routers
from .views import CollectionViewSet, BookMarkViewSet

router = routers.DefaultRouter()

router.register(r'collections', CollectionViewSet)
router.register(r'bookmarks', BookMarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
