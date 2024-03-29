from rest_framework import routers

from product.api.v1.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
