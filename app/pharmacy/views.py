
from rest_framework import generics

from django_filters import rest_framework as filters
# Create your views here.

from .models import Pharmacy
from .filters import PharmacyLocationFilterSet
from .serializers import PharmacySerializer

class PharmaciesListAPI(generics.ListAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PharmacyLocationFilterSet

class PharmacyCreateAPIView(generics.CreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class PharmacyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer