

from math import radians, cos, sin, asin, sqrt

from django.db import models

from phonenumber_field import modelfields



class Location(models.Model):
    """
    """
    
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Ширина")
    
    address = models.CharField(unique=True, verbose_name="Адресс")
    
    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
        
    
    def distance(self, location: "Location") -> float:
        lon1, lat1, lon2, lat2 = map(radians, [self.latitude, self.longitude, 
                                               location.latitude, location.longitude])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        dist = 6371000 * c
        return dist
    
    def save(self, *args, **kwargs) -> None:
        if not (-90 <= self.latitude <= 90):
            raise ValueError("latitude must between [-90; +90]")
        if not (0 <= self.longitude <= 180):
            raise ValueError("longitude must between [0; +180]")
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"({self.latitude}, {self.longitude})"


class Pharmacy(models.Model):

    phone = modelfields.PhoneNumberField(region='RU', 
                                         unique=True)
    
    email = models.EmailField(unique=True, 
                              verbose_name="email")
    
    location = models.OneToOneField(Location,
                                    on_delete=models.SET_NULL, 
                                    null=True, blank=True, 
                                    verbose_name="Место расположения")
    
    beginning_of_work = models.TimeField(verbose_name="Начало работы")
    end_of_work = models.TimeField(verbose_name="Конец работы")
    
    class Meta:
        verbose_name = 'Аптека'
        verbose_name_plural = 'Аптеки'
        
    def save(self, *args, **kwargs) -> None:
        if self.beginning_of_work > self.end_of_work:
            raise ValueError("beginning_of_work must less end_of_work")
        return super().save(*args, **kwargs)    
    
    def __str__(self) -> str:
        return "Аптека по адресу: " + str(self.location)
        