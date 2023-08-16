#  endpoints
from django.http import JsonResponse
from .places import Place
from .attractions import Attraction
from .user import User
from .comments import Comment
from .serializers import PlaceSerializer
from .serializers import AttractionSerializer
from .serializers import CommentSerializer
from .serializers import UserSerializer
from urllib.parse import unquote

from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render



@api_view(['GET'])
def get_place_list(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return JsonResponse({'places': serializer.data})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_place(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_one_place(request, place_id):
    try:
        places = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaceSerializer(places)
    return JsonResponse({'places': serializer.data})


# Delete a place by id
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_one_place(request, place_id):
    try:
        places = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    places.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ====================================================
# one_to_many
@api_view(['GET'])
def get_place_attractions(request, place_id):
    try:
        # this is just to make sure the place is available
        place = Place.objects.get(pk=place_id)
        attractions = Attraction.objects.filter(place_id=place_id)
        serializer = AttractionSerializer(attractions, many=True)
        return Response({'attractions': serializer.data})
    except Place.DoesNotExist:
        return Response(status=404, data={'message': 'Place not found'})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_attraction(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return Response(status=404, data={'message': 'Place not found'})

    # if request.method == 'POST':
    data = request.data.copy()
    data['place'] = place.id
    serializer = AttractionSerializer(data=data)
    if serializer.is_valid():
        attraction = serializer.save()  # Place will be set automatically
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delte a specific attraction in a specific place
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_attraction(request, place_id, attraction_id):
    try:
        place = Place.objects.get(id=place_id)
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
        attraction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except (Place.DoesNotExist, Attraction.DoesNotExist):
        return Response(status=404, data={'message': 'Place or Attraction not found'})


@api_view(['PATCH'])
def like_attraction(request, place_id, attraction_id):
    try:
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
    except Attraction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Increment the 'likes' field by 1
    attraction.likes += 1
    attraction.save()

    serializer = AttractionSerializer(attraction)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def dislike_attraction(request, place_id, attraction_id):
    try:
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
    except Attraction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    attraction.dislike += 1
    attraction.save()

    serializer = AttractionSerializer(attraction)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def favorite_attraction(request, place_id, attraction_id):
    try:
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
    except Attraction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if attraction.favorite:
        attraction.favorite = False
    else:
        attraction.favorite = True

    attraction.save()

    serializer = AttractionSerializer(attraction)
    return Response(serializer.data, status=status.HTTP_200_OK)

# ======================
@api_view(['GET'])
def get_comment_attraction(request, place_id, attraction_id):
    try:
        place = Place.objects.get(id=place_id)
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
        comments = Comment.objects.filter(attraction_id=attraction_id)
        serializer = CommentSerializer(comments, many=True)
        return Response({'comments': serializer.data})
    except (Place.DoesNotExist, Attraction.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Place or Attraction not found'})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_comment_attraction(request, place_id, attraction_id):
    try:
        place = Place.objects.get(id=place_id)
        attraction = Attraction.objects.get(
            id=attraction_id, place_id=place_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Associate comment with the attraction
            serializer.save(attraction_id=attraction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except (Place.DoesNotExist, Attraction.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Place or Attraction not found'})

# get one user by id
@api_view(['GET'])
def get_user(request, username):
    try:
        decoded_username = unquote(username)
        user = User.objects.get(username=decoded_username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)

    if request.method == 'GET':
        return Response({'user': serializer.data})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_favorite_attractions(request):
    favorite_attractions = Attraction.objects.filter(favorite=True)
    attractions_data = [
        {
            "id": attr.id,
            "name": attr.name,
            "image": attr.image.url,
            "place_id": attr.place_id.id,

        }
        for attr in favorite_attractions
    ]
    return JsonResponse({"attractions": attractions_data})


@api_view(['GET'])
def get_user_posted_attractions(request, user_id):
    posted_attractions = Attraction.objects.filter(created_by=user_id)
    attractions_data = [
        {
            "id": attr.id,
            "name": attr.name,
            "image": attr.image.url,
            "place_id": attr.place_id.id,
        }
        for attr in posted_attractions
    ]
    return JsonResponse({"attractions": attractions_data})


@api_view(['DELETE'])
def delete_user_posted_attraction(request, attraction_id):
    try:
        attraction = Attraction.objects.get(id=attraction_id)

        username_param = request.GET.get("username")

        if attraction.created_by != username_param:
            return Response({"message": "You are not authorized to delete this attraction."}, status=403)

        attraction.delete()
        return Response({"message": "Attraction deleted successfully."})
    except Attraction.DoesNotExist:
        return Response({"message": "Attraction not found."}, status=404)

