# product/serializers.py

from rest_framework import serializers

from .models import Medicine



class MedicinalDrugSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Medicine
        fields = '__all__'