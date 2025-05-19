from products.models import MediaFile
from rest_framework import serializers

class MediaFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['name', 'slug']