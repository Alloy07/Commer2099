from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from products.models import ProductVariant
from products.api_endpoints.ProductVariantList.serializers import ProductVariantListSerializer




 

class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][ProductVariantListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class ProductVariantRetrieveAPIView(RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][ProductVariantRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
