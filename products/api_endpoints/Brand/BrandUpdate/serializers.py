from products.models import Brand
from rest_framework import serializers

class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug']