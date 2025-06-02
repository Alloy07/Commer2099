from products.models import ProductVariant
from rest_framework import serializers

class ProductVariantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ("id", "name")


