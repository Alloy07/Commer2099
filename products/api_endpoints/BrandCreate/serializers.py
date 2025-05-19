from products.models import Brand
from rest_framework import serializers

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug']
    