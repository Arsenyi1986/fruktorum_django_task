from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Collection, BookMark
from .serializers import CollectionSerializer, BookMarkSerializer


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()


class BookMarkViewSet(ModelViewSet):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()