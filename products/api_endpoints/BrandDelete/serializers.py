from products.models import Brand
from rest_framework import serializers

class BrandDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "slug")
