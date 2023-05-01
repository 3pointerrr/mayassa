from rest_framework import viewsets
from rest_framework.renderers import JSONOpenAPIRenderer

from product.models import Product
from product.api.v1.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    allowed_methods = ['GET']
    serializer_class = ProductSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'

    #tolid file json
    renderer_classes=[
        JSONOpenAPIRenderer,
    ]