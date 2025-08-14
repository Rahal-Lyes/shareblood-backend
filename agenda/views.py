# views.py
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    def get_queryset(self):
        # Facultatif : filtrer uniquement les événements de l'utilisateur connecté
        user = self.request.user
        return Event.objects.filter(user=user)

