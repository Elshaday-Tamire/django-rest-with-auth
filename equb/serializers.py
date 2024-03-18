from rest_framework import serializers
from .models import Equb,EqubType

class EqubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equb
        fields ='__all__'
    
class EqubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqubType
        fields ='__all__'