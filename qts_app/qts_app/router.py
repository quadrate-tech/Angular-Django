from qts_api.viewsets import ad_typeViewSet
from rest_framework import routers
from qts_api.viewsets import districtViewSet


router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)

#District router
router.register('district',districtViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

