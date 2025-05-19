from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from products.models import MediaFile
from products.api_endpoints.MediaFileList.serializers import MediaFileListSerializer
  

class MediaFileListAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][MediaFileListAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    

class MediaFileRetrieveAPIView(RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][MediaFileRetrieveAPIView]", request, args, kwargs)
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
