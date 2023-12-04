from django.shortcuts import render
from rest_framework import generics

from django_filters import rest_framework as filters


from .models import Medicine
from .filters import MedicinalDrugFilter
from .serializers import MedicinalDrugSerializer

class MedicinesListAPI(generics.ListAPIView):
    
    queryset = Medicine.objects.all()
    serializer_class = MedicinalDrugSerializer
    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MedicinalDrugFilter
    

class MedicineCreateAPIView(generics.CreateAPIView):

    queryset = Medicine.objects.all()
    serializer_class = MedicinalDrugSerializer


class MedicineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Medicine.objects.all()
    serializer_class = MedicinalDrugSerializer