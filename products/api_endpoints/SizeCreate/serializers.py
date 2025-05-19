from products.models import Size
from rest_framework import serializers

class SizeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name', 'slug']
        