from rest_framework.generics import UpdateAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariant.ProductVariantUpdate.serializers import ProductVariantUpdateSerializer


class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer
