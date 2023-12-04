
from rest_framework import generics

from django_filters import rest_framework as filters

from .models import PharmacyMedicinalDrugPrice
from .serializers import PharmacyMedicinalDrugPriceSerializer
from .filters import PharmacyMedicinalDrugPriceFilterSet



class PharmaciesMedicinalsPriceListAPI(generics.ListAPIView, generics.CreateAPIView):
    queryset = PharmacyMedicinalDrugPrice.objects.all()
    serializer_class = PharmacyMedicinalDrugPriceSerializer
    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PharmacyMedicinalDrugPriceFilterSet
    
class PharmacyMedicinalPriceCreateAPIView(generics.CreateAPIView):
    queryset = PharmacyMedicinalDrugPrice.objects.all()
    serializer_class = PharmacyMedicinalDrugPriceSerializer

class PharmacyMedicinalPriceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PharmacyMedicinalDrugPrice.objects.all()
    serializer_class = PharmacyMedicinalDrugPriceSerializer