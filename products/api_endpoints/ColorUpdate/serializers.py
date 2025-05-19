from products.models import Color
from rest_framework import serializers

class ColorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'slug']