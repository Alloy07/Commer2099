from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from products.models import Brand
from products.api_endpoints.BrandList.serializers import BrandListSerializer
  

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][BrandListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][BrandRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
