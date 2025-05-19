from products.models import MediaFile
from rest_framework import serializers

class MediaFileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['name', 'slug']