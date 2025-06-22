from rest_framework.generics import UpdateAPIView
from rest_framework import permissions

from products.models import History
from products.api_endpoints.History.HistoryUpdate.Serializers import HistoryUpdateSerializer


class HistoryUpdateAPIView(UpdateAPIView):
    queryset = History.objects.filter(is_active=True)
    serializer_class = HistoryUpdateSerializer
    permission_classes = [permissions.IsAdminUser]