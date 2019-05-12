from rest_framework import routers

from .api import RealtorViewSet


router = routers.DefaultRouter()
router.register('api/realtors', RealtorViewSet, 'realtors')

urlpatterns = router.urls
