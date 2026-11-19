from rest_framework import serializers
from .models import Brand, Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "country"]

class CarSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    fuel_type_display = serializers.CharField(source="get_fuel_type_display", read_only=True)

    class Meta:
        model = Car
        fields = [
            "id", "author", "name", "year", "price",
            "publishing_house", "page_count", "genre",
            "popular", "status",
            "ISBN", "description", "created_at",
        ]
        read_only_fields = ["created_at"]
