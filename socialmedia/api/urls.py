from rest_framework import routers

from socialmedia.api.v1.views import SocialMediaViewSet

router = routers.DefaultRouter()
router.register(r'socialmedias', SocialMediaViewSet)

urlpatterns = router.urls
