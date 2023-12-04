from django.contrib import admin

# Register your models here.

from .models import Location, Pharmacy


admin.site.register([
    Location,
    Pharmacy
])