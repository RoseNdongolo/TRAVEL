from rest_framework import serializers
from . models import *

class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = '__all__'

class AttractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attraction
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    destination = serializers.SlugRelatedField(slug_field='name', queryset=Destination.objects.all())

    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'