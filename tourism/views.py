from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializers import *



def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api(request, pk=None):
        if request.method == 'GET':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoestNotExist:
                    return Response({'messsage': 'Error Getting Data'})
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)
            
        elif request.method == 'POST':
            serializer = serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = serializer_class(instance, data=request.data )
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'object not found for update'})
                
        elif request.method == 'DELETE':
            try:
                instance = model_class.objects.get(pk=pk)
                instance.delete()
                return Response({'message': 'deleted successfully'})
            except model_class.DoesNotExist:
                return Response({'message': 'iD NOT FOUND'}) 

  
    return api


@api_view(['GET'])
def curent_user(request):
    user = request.user
    return Response(user)


manage_destination = generic_api(Destination, DestinationSerializer)
manage_attraction = generic_api(Attraction, AttractionSerializer)
manage_review = generic_api(Review, ReviewSerializer)
manage_booking = generic_api(Booking, BookingSerializer)
manage_user = generic_api(User, UserSerializer)

