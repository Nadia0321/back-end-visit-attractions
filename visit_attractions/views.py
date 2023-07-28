#  endpoints
from django.http import JsonResponse
from .places import Place
from .attractions import Attraction
from .serializers import PlaceSerializer
from .serializers import AttractionSerializer
from .serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

@api_view(['GET', 'POST', 'DELETE'])
def place_list(request):
    # get all places
    if request.method == 'GET':
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return JsonResponse({'places': serializer.data})

    # post a place
    if request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete a place


# get one place
@api_view(['GET'])
def get_one_place(request, place_id):
    places = validate_model(Place, place_id)
    serializer = PlaceSerializer(places)
    return JsonResponse({'places': serializer.data})


def validate_model(cls, id):
    try:
        # id = int(id)
        model = cls.objects.get(pk=id)
    except cls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return model











