#  endpoints
from django.http import JsonResponse
from .places import Place
from .attractions import Attraction
from .serializers import PlaceSerializer
from .serializers import AttractionSerializer
from .serializers import CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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


# @api_view(['GET', 'POST'])
# def attractions_list(request, place_id):
#     # get all attractions
#     if request.method == 'GET':
#         attractions = Attraction.objects.all()
#         serializer = AttractionSerializer(attractions, many=True)
#         return JsonResponse({'attractions': serializer.data})

#     # post an attraction
#     if request.method == 'POST':
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def one_attraction(request):
#     # get all attractions
#     if request.method == 'GET':
#         attractions = Attraction.objects.all()
#         serializer = AttractionSerializer(attractions, many=True)
#         return JsonResponse({'attractions': serializer.data})

#     # post an attraction
#     if request.method == 'POST':
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # response = get_object_or_404(cls, id)
    # return JsonResponse(response.data)


# def validate_model(cls, id):
#     try:
#         # id = int(id)
#         model = cls.objects.get(pk=id)
#     except cls.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     return model

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
