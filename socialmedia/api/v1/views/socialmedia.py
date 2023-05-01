from rest_framework import viewsets
from rest_framework.renderers import JSONOpenAPIRenderer

from socialmedia.models import SocialMedia
from socialmedia.api.v1.serializers import SocialMediaSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    allowed_methods = ['GET']
    serializer_class = SocialMediaSerializer
    renderer_classes=[
        JSONOpenAPIRenderer,
    ]