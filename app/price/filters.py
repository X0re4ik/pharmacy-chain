
from django_filters import rest_framework as filters

from .models import PharmacyMedicinalDrugPrice


class PharmacyProductPriceFilterSet(filters.FilterSet):
    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte', label="Цена меньше, чем ...")
    price__gte = filters.NumberFilter(field_name='price', lookup_expr='gte', label="Цена больше, чем ...")
    

class PharmacyMedicinalDrugPriceFilterSet(PharmacyProductPriceFilterSet):
    
    class Meta:
        model = PharmacyMedicinalDrugPrice
        fields = '__all__'