
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from .filters import CustomUserFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination

from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

# views.py

@api_view(['GET'])
def donors_by_bloodtype(request):
    data = (
        CustomUser.objects.filter(is_donor=True)
        .values("blood_type")
        .annotate(total=Count("id"))
        .order_by("blood_type")
    )

    labels = [item["blood_type"] for item in data]
    values = [item["total"] for item in data]

    return Response({
        "labels": labels,
        "datasets": [{
            "label": "Nombre de donneurs par groupe sanguin",
            "data": values,
            "backgroundColor": [
                "red", "blue", "green", "orange", "purple", "cyan", "pink", "yellow"
            ],
        }]
    })
    