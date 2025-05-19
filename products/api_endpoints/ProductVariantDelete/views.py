from rest_framework.generics import DestroyAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariantDelete.serializers import ProductVariantDeleteSerializer

class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)