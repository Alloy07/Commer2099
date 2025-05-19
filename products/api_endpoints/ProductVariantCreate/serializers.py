from products.models import ProductVariant
from rest_framework import serializers

class ProductVariantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['name', 'slug']
        