from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from products.models import History
from products.api_endpoints.History.HistoryList.Serializers import HistoryListSerializer


class HistoryListAPIView(ListAPIView):
    queryset = History.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = HistoryListSerializer
    permission_classes = [permissions.IsAuthenticated]


class HistoryRetrieveAPIView(RetrieveAPIView):
    queryset = History.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = HistoryListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"