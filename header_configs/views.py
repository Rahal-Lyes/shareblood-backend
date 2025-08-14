# views.py

from rest_framework import viewsets
from .models import TableConfig, HeaderConfig
from .serializers import TableConfigSerializer, HeaderConfigSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class TableConfigViewSet(viewsets.ModelViewSet):
    queryset = TableConfig.objects.all()
    serializer_class = TableConfigSerializer
    lookup_field = "endpoint"  # permet d'accéder via /tables/<endpoint>/

    @action(detail=True, methods=["get"])
    def headers(self, request, endpoint=None):
        try:
            table = self.get_object()
        except TableConfig.DoesNotExist:
            return Response({"error": "Table not found"}, status=404)

        headers = table.headers.order_by("order")
        serializer = HeaderConfigSerializer(headers, many=True)
        return Response(serializer.data)


class HeaderConfigViewSet(viewsets.ModelViewSet):
    queryset = HeaderConfig.objects.all()
    serializer_class = HeaderConfigSerializer
