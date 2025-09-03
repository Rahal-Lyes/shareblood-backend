from rest_framework.response import Response
from .models import Category,Product
from rest_framework import generics
from .serializers import ProductSerializer,CategorySerializer

class ProductList(generics.ListCreateAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
