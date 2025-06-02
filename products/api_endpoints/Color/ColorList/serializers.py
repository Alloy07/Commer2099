from products.models import Color
from rest_framework import serializers

class ColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name", "slug")


