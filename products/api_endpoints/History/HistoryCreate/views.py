from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework import parsers

from products.models import History
from products.api_endpoints.History.HistoryCreate.Serializers import HistoryCreateSerializer



class HistoryCreateAPIView(CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]