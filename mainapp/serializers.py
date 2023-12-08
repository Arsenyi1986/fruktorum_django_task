from rest_framework.serializers import ModelSerializer
from .models import Collection, BookMark


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"


class BookMarkSerializer(ModelSerializer):
    class Meta:
        model = BookMark
        fields = "__all__"