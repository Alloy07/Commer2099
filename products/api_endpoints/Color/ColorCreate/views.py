from rest_framework.generics import CreateAPIView

from products.models import Color
from products.api_endpoints.Color.ColorCreate.serializers import ColorCreateSerializer


class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    