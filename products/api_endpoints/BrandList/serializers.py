from products.models import Brand
from rest_framework import serializers

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "slug")


