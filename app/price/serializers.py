from rest_framework import serializers

from .models import PharmacyMedicinalDrugPrice



class PharmacyMedicinalDrugPriceSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = PharmacyMedicinalDrugPrice
        fields = '__all__'