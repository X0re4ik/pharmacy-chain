from django.contrib import admin
from django.urls import path

from .views import (PharmaciesListAPI,
                    PharmacyCreateAPIView,
                    PharmacyRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('pharmacies', PharmaciesListAPI.as_view(), name="pharmacies"),
    
    path('pharmacies/<str:pk>', PharmacyRetrieveUpdateDestroyAPIView.as_view(), 
         name="pharmacy-retrieve-update-destroy"),
    
    path('pharmacy', PharmacyCreateAPIView.as_view(), 
         name="pharmacy-create")
]
