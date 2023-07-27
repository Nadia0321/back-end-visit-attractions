from rest_framework import serializers
from .places import Place
from .attractions import Attraction
from .comments import Comment


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name']
