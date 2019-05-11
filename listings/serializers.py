from rest_framework import serializers
from .models import Listing


# Listing Serializer
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
