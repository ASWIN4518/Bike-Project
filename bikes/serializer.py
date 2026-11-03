from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
    Fuel_type=serializers.CharField(max_length=200)
    bike_name=serializers.CharField(max_length=200)
    def validate_Fuel_type(self, value):
        if value=="Petrol":
            return value
        else:
            raise serializers.ValidationError("Other fuel cannot be valid")

    def validate_bike_name(self,value):
        if value and value[0].isupper():
            return value
        else:
            raise serializers.ValidationError("Starting letter should Capital ")
        
    class Meta():
        model=Bike
        fields="__all__"

