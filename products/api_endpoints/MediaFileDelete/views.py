from rest_framework.generics import DestroyAPIView

from products.models import MediaFile
from products.api_endpoints.MediaFileDelete.serializers import MediaFileDeleteSerializer


class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)