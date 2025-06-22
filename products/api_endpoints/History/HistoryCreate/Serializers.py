from rest_framework.serializers import ModelSerializer

from products.models import History

class HistoryCreateSerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ["title", "product", "image"]