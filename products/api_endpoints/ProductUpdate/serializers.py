from rest_framework import serializers

from products.models import Product


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "brand",
        ]
    
