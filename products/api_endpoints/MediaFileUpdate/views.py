from rest_framework.generics import UpdateAPIView

from products.models import MediaFile
from products.api_endpoints.MediaFileUpdate.serializers import MediaFileUpdateSerializer


class MediaFileUpdateAPIView(UpdateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileUpdateSerializer
