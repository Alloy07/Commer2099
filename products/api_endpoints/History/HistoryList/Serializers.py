from rest_framework.serializers import ModelSerializer

from products.models import History

class HistoryListSerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "title", "product", "image"]
        read_only_fields = ["id"]