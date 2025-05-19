from products.models import Color
from rest_framework import serializers

class ColorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'slug']
        