
from django.urls import path


from .views import (MedicinesListAPI, 
                    MedicineRetrieveUpdateDestroyAPIView,
                    MedicineCreateAPIView)

urlpatterns = [
    path('medicinals', MedicinesListAPI.as_view(), name="medicinals-list"),
    
    path('medicinals/<str:pk>', MedicineRetrieveUpdateDestroyAPIView.as_view(), 
         name="medicinals-retrieve-update-destroy"),
    
    path('medicinal', MedicineCreateAPIView.as_view(), 
         name="medicinals-create"), 
]
