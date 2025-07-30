# users/filters.py
import django_filters
from .models import CustomUser

class CustomUserFilter(django_filters.FilterSet):
    is_donor = django_filters.BooleanFilter(field_name='is_donor')
    blood_type = django_filters.ChoiceFilter(choices=CustomUser._meta.get_field('blood_type').choices)
    wilaya = django_filters.CharFilter(lookup_expr='icontains')  # Recherche partielle (non sensible à la casse)

    class Meta:
        model = CustomUser
        fields = ['is_donor', 'blood_type', 'wilaya']

