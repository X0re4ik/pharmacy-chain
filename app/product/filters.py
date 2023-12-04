
from django_filters import rest_framework as filters

from .models import Medicine, Product


class ProductFilter(filters.FilterSet):
    exist_instruction = filters.BooleanFilter(method='filter_exist_instruction',
                                               label="Есть инструкция?")
    
    exist_photo = filters.BooleanFilter(method='filter_exist_photo',
                                        label="Есть фото?")
        
    def filter_exist_photo(self, queryset, name, value):
        if value: return queryset.exclude(photo=None).all()
        return queryset.filter(photo=None).all()
    
    def filter_exist_instruction(self, queryset, name, value):
        if value: return queryset.exclude(instruction=None).all()
        return queryset.filter(instruction=None).all()



class MedicinalDrugFilter(ProductFilter):
    
    class Meta:
        model = Medicine
        fields = ['exist_instruction', 'exist_photo', 'need_recipe']