from rest_framework.generics import CreateAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariantCreate.serializers import ProductVariantCreateSerializer


class ProductVariantCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    