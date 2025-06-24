from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import History

class HistoryDeleteAPIView(DestroyAPIView):
    queryset = History.objects.filter(is_active=True)
    permission_classes = [permissions.IsAdminUser]