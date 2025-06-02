from products.models import Size
from rest_framework import serializers

class SizeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "name", "slug")
