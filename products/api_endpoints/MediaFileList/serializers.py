from products.models import MediaFile
from rest_framework import serializers

class MediaFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ("id", "name", "slug")


