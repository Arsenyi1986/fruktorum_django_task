from rest_framework import serializers
from .models import Collection, Link, ParsedData

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'user']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url']

class ParsedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParsedData
        fields = ['id', 'link', 'title', 'description', 'link_type', 'image', 'collections']