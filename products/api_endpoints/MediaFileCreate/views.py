from rest_framework.generics import CreateAPIView

from products.models import MediaFile
from products.api_endpoints.MediaFileCreate.serializers import MediaFileCreateSerializer


class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer

    def post(self, request, *args, **kwargs):   
        print( request, args, kwargs)
        return super().post(request, *args, **kwargs)
    