from rest_framework.generics import CreateAPIView

from products.models import Product
from products.api_endpoints.Product.ProductCreate.serializers import ProductCreateSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    