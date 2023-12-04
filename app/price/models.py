from django.db import models

from django.core.validators import (MaxLengthValidator, MinLengthValidator, 
                                    MaxValueValidator, MinValueValidator)

from product.models import Medicine
from pharmacy.models import Pharmacy



class PharmacyProductPrice(models.Model):
    
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, verbose_name="Аптека")
    price = models.FloatField(validators=[MaxValueValidator(1_000_000), MinValueValidator(1)],
                              verbose_name="Цена в рублях")

    class Meta:
        verbose_name = 'Цена на продукт в аптеке'
        verbose_name_plural = 'Цены на продукты в аптеках'
        abstract = True
    
    def __str__(self) -> str:
        raise ValueError("Перелпределите метод __str__")


class PharmacyMedicinalDrugPrice(PharmacyProductPrice):
    
    medicinal_drug = models.ForeignKey(Medicine, 
                                       on_delete=models.CASCADE, 
                                       verbose_name="Лекартственный препарат")
    
    class Meta:
        verbose_name = 'Цена на лакарство в аптеке'
        verbose_name_plural = 'Цены на лакарства в аптеках'
        constraints = [
            models.UniqueConstraint(fields=['pharmacy', 'medicinal_drug'], name='pharmacy_medicinal_drug')
        ]
    
    
    def __str__(self) -> str:
        return str(self.pharmacy) + " - " + str(self.medicinal_drug) + ": " + str(self.price)