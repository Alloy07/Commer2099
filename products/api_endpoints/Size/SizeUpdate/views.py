from rest_framework.generics import UpdateAPIView

from products.models import Size
from products.api_endpoints.Size.SizeUpdate.serializers import SizeUpdateSerializer


class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
