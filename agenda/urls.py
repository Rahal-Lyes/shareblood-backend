from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, events_per_month, events_per_user, reservation_rate

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path("events-per-month/", events_per_month, name="events_per_month"),
    path("events-per-user/", events_per_user, name="events_per_user"),
    path("reservation-rate/", reservation_rate, name="reservation_rate"),
]
