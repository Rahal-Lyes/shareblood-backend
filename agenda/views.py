from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.db.models import Q

from django.db.models.functions import TruncMonth
from django.db.models import Count
from rest_framework.decorators import api_view
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        start = request.data.get("start")
        end = request.data.get("end")

        # Vérifier s’il y a un chevauchement
        overlap = Event.objects.filter(
            Q(start__lt=end) & Q(end__gt=start)  # chevauchement
        ).exists()

        if overlap:
            return Response(
                {"error": "Ce créneau est déjà réservé."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

# stats/views.py


@api_view(["GET"])
def events_per_month(request):
    stats = (
        Event.objects.annotate(month=TruncMonth("start"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )
    labels = [item["month"].strftime("%B %Y") for item in stats]
    data = [item["total"] for item in stats]
    return Response({"labels": labels, "data": data})


@api_view(["GET"])
def events_per_user(request):
    stats = (
        Event.objects.values("user__username")
        .annotate(total=Count("id"))
        .order_by("-total")
    )
    labels = [item["user__username"] for item in stats]
    data = [item["total"] for item in stats]
    return Response({"labels": labels, "data": data})

@api_view(["GET"])
def reservation_rate(request):
    stats = (
        Event.objects.values("reserved")
        .annotate(total=Count("id"))
        .order_by("reserved")
    )
    labels = ["Réservé" if item["reserved"] else "Libre" for item in stats]
    data = [item["total"] for item in stats]
    return Response({"labels": labels, "data": data})  