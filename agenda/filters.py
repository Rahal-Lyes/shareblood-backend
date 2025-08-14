import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    start__gte = django_filters.DateTimeFilter(field_name="start", lookup_expr="gte")
    start__lte = django_filters.DateTimeFilter(field_name="start", lookup_expr="lte")
    user = django_filters.NumberFilter(field_name="user_id")

    class Meta:
        model = Event
        fields = ['user', 'start__gte', 'start__lte']
