from typing import Optional

from rest_framework import serializers

from .models import Pharmacy, Location


class LocationSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Location
        fields = '__all__'



class PharmacySerializer(serializers.ModelSerializer):
    """"""
    location = LocationSerializer(allow_null=True, required=False)
    
    class Meta:
        model = Pharmacy
        fields = '__all__'
        
    def create(self, validated_data):
        location = self._get_location(validated_data)
        pharmacy = super().create(validated_data)
        pharmacy.location = location
        pharmacy.save()
        return pharmacy
    
    def _get_location(self, validated_data) -> Optional[Location]:
        location = validated_data.pop("location", None)
        location_serializer = LocationSerializer(data=location)
        location_serializer.is_valid(raise_exception=True)
        return location_serializer.create(location_serializer.data)