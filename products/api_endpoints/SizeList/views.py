from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from products.models import Size
from products.api_endpoints.SizeList.serializers import SizeListSerializer


class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][SizeListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][SizeRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
