# serializers.py

from rest_framework import serializers
from .models import TableConfig, HeaderConfig


class HeaderConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderConfig
        fields = [
            "id", "key", "display_name", "help_text", "field_type",
            "sortable", "visible", "width", "order"
        ]


class TableConfigSerializer(serializers.ModelSerializer):
    headers = HeaderConfigSerializer(many=True, read_only=True)

    class Meta:
        model = TableConfig
        fields = [
            "id", "endpoint", "display_name", "description", "headers"
        ]
