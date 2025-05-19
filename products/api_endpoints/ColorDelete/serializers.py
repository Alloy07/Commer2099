from products.models import Color
from rest_framework import serializers

class ColorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name", "slug")
