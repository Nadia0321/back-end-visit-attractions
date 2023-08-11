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

from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from .models import Place
# from .models import BlogPost
from django.shortcuts import render

# from rest_framework_simplejwt.tokens import RefreshToken
# @api_view(['GET'])
# def get_place_list(request):

#     places = Place.objects.all()
#     serialized_places = []

#     for place in places:
#         serialized_place = {
#             'name': place.name,
#             'description': place.description,
#             'country': place.country,
#             'city': place.city,
#             'image_url': place.image.url,  # Generate the S3 URL
#         }
#         serialized_places.append(serialized_place)

#     return JsonResponse({'places': serialized_places})


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

# class PlaceCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         name = request.data.get("name")
#         description = request.data.get("description")
#         country = request.data.get("country")
#         city = request.data.get("city")
#         image = request.data.get("image")

#         if name and description and country and city and image:
#             # Upload the image to S3 or another storage service and get the URL
#             image_url = upload_image_to_s3(image)

#             # Create a new Place instance with the image URL
#             place = Place.objects.create(
#                 name=name, description=description, country=country,
#                 city=city, image=image_url
#             )

#             return Response({"message": "Place created successfully."}, status=201)
#         else:
#             return Response({"message": "Invalid data provided."}, status=400)

# get one place by id


@api_view(['GET'])
def get_one_place(request, place_id):
    try:
        places = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaceSerializer(places)
    # if not serializer.is_valid():
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    # serializer = PlaceSerializer(places)
    # if serializer.is_valid():
    #     serializer.delete()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    data['place'] = place.id  # Set the place ID in the data
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

    # Increment the 'likes' field by 1
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

    # Increment the 'likes' field by 1
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
# ============================================================


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


def get_all_favorite_attractions(request):
    favorite_attractions = Attraction.objects.filter(favorite=True)
    attractions_data = [
        {
            "id": attr.id,
            "name": attr.name,
            "description": attr.description,
            "place_id": attr.place_id.id,

        }
        for attr in favorite_attractions
    ]
    return JsonResponse({"attractions": attractions_data})


# def home(request):
#     return render(request, 'home.html', {'posts':BlogPost.object.all()})


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
