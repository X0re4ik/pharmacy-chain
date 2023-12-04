
from typing import Tuple
from django.core.validators import EMPTY_VALUES

from django_filters import rest_framework as filters

from .models import Pharmacy


class PharmacyLocationFilterSet(filters.FilterSet):
    class Meta:
        model = Pharmacy
        fields = '__all__'