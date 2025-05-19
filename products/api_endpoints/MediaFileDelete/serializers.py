from products.models import MediaFile
from rest_framework import serializers

class MediaFileDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ("id", "name", "slug")
