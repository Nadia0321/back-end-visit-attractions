#  endpoints
from django.http import JsonResponse
from .places import Place
from .attractions import Attraction
from .user import User
from .serializers import PlaceSerializer
from .serializers import AttractionSerializer
from .serializers import CommentSerializer
from .serializers import UserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def get_place_list(request):
    # get all places
    # if request.method == 'GET':
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return JsonResponse({'places': serializer.data})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_place(request):
    # post a place
    # if request.method == 'POST':
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get one place
@api_view(['GET'])
def get_one_place(request, place_id):
    try:
        places = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaceSerializer(places)
    # if not serializer.is_valid():
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return JsonResponse({'places': serializer.data})


# Delete a place
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def delete_one_place(request, place_id):
    try:
        places = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaceSerializer(places)
    if serializer.is_valid():
        serializer.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    if request.method == 'POST':
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(place_id=place_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# get one user by id
@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)

    if request.method == 'GET':
        return JsonResponse({'user': serializer.data})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HomeView(APIView):

#    permission_classes = (IsAuthenticated, )
#    def get(self, request):
#        content = {'message': 'Welcome!'}
#        return Response(content)

# class LogoutView(APIView):
#      permission_classes = (IsAuthenticated,)
#      def post(self, request):

#           try:
#                refresh_token = request.data["refresh_token"]
#                token = RefreshToken(refresh_token)
#                token.blacklist()
#                return Response(status=status.HTTP_205_RESET_CONTENT)
#           except Exception as e:
#                return Response(status=status.HTTP_400_BAD_REQUEST)
