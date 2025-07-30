
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from .filters import CustomUserFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination

class RegisterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field='id'
    

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomUserFilter
    pagination_class = CustomPagination  
    