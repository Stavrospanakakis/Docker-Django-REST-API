from rest_framework import routers
from .api import PersonViewSet

router = routers.DefaultRouter()
router.register('api/persons', PersonViewSet, 'person')

urlpatterns = router.urls