from rest_framework import serializers
from .models import Realtor


# Realtor Serializer
class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'
