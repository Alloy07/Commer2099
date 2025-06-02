from rest_framework.generics import DestroyAPIView

from products.models import Size
from products.api_endpoints.Size.SizeDelete.serializers import SizeDeleteSerializer


class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)