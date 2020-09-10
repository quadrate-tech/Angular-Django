from qts_api.viewsets import ad_typeViewSet
from rest_framework import routers

from qts_api.viewsets import paymentViewSet

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)

router = routers.DefaultRouter()
router.register('payment', paymentViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

