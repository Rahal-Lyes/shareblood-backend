# backend/pdf_tools/urls.py
from django.urls import path
from .views import PDFToJPGView

urlpatterns = [
    path('pdf-to-jpg/', PDFToJPGView.as_view(), name='pdf-to-jpg'),
]