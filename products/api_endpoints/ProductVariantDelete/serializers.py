from products.models import ProductVariant
from rest_framework import serializers

class ProductVariantDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ("id", "name", "slug")
