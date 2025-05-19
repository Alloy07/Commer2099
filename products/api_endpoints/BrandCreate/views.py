from rest_framework.generics import CreateAPIView

from products.models import Brand
from products.api_endpoints.BrandCreate.serializers import BrandCreateSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    