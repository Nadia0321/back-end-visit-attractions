from rest_framework import serializers
from .places import Place
from .attractions import Attraction
from .comments import Comment
from .user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'description',
                  'country', 'city', 'image']


class AttractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attraction
        fields = ['id', 'name', 'likes', 'dislike',
                  'description', 'favorite', 'place_id', 'image', 'created_by']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'attraction_id', 'username']
