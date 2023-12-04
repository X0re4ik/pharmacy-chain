from django.contrib import admin

# Register your models here.

from .models import PharmacyMedicinalDrugPrice


admin.site.register([
    PharmacyMedicinalDrugPrice
])