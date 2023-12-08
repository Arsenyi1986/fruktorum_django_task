from rest_framework import viewsets
from .models import Collection, Link, ParsedData
from .serializers import CollectionSerializer, LinkSerializer, ParsedDataSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class ParsedDataViewSet(viewsets.ModelViewSet):
    serializer_class = ParsedDataSerializer
    queryset = ParsedData.objects.all()