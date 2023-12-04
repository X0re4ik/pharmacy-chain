# product/models.py

import uuid

from django.db import models
from django.core.validators import (MaxLengthValidator, MinLengthValidator, 
                                    MaxValueValidator, MinValueValidator)


class Product(models.Model):
    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    
    manufacturer = models.CharField(validators=[MinLengthValidator(1), MaxLengthValidator(30)])
    
    name = models.CharField(validators=[MaxLengthValidator(100), MinLengthValidator(5)],
                            unique=True)
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        abstract = True
    
    def __str__(self) -> str:
        raise ValueError("Переопределите метод __str__")
    


class Medicine(Product):
    
    need_recipe = models.BooleanField(verbose_name="Нужен ли рецепт?")
    
    number_of_tablets = models.IntegerField(validators=[MinValueValidator(1)], 
                                            blank=True, null=True, 
                                            verbose_name="Количество таблеток")
    
    dosage = models.IntegerField(validators=[MinValueValidator(1)],
                                 blank=True, null=True, 
                                 verbose_name="Дозировка")
    
    class Meta:
        verbose_name = 'Лекартсвенный препарат'
        verbose_name_plural = 'Лекартсвенные препараты'
        
    
    def __str__(self) -> str:
        return self.name
    