from rest_framework.generics import DestroyAPIView

from products.models import Product
from products.api_endpoints.Product.ProductDelete.serializers import ProductDeleteSerializer


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)