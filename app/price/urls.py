from django.contrib import admin
from django.urls import path

from .views import (PharmaciesMedicinalsPriceListAPI, 
                    PharmacyMedicinalPriceRetrieveUpdateDestroyAPIView,
                    PharmacyMedicinalPriceCreateAPIView)

urlpatterns = [
    path('prices', PharmaciesMedicinalsPriceListAPI.as_view(), name="prices"),
    
    path('prices/<str:pk>', 
         PharmacyMedicinalPriceRetrieveUpdateDestroyAPIView.as_view(), 
         name="price-retrieve-update-destroy"),
    
    path('price', PharmacyMedicinalPriceCreateAPIView.as_view(), name="price-create"), 
]
