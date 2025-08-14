# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableConfigViewSet, HeaderConfigViewSet

router = DefaultRouter()
router.register(r"tables", TableConfigViewSet)
router.register(r"headers", HeaderConfigViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
