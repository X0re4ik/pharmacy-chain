from django.test import TestCase
from pharmacy.filters import PharmacyLocationFilterSet

from pharmacy.models import Location, Pharmacy
from django.utils.timezone import datetime, timedelta

class PharmacyLocationFilterSetTestCase(TestCase):
    
    
    def setUp(self) -> None:
        
        self._location = Location.objects.create(longitude=56,
                                                 latitude=87)
        
        
        self._pharmacy = Pharmacy.objects.create(location=self._location, 
                                beginning_of_work=datetime.now(),
                                end_of_work=datetime.now())
        
    
    def test_location(self):
        qs = Pharmacy.objects.all()
        f = PharmacyLocationFilterSet(data={'location': '(dsd, sada)'}, queryset=qs)
        result = f.qs
        print(result)
        