from qts_api.viewsets import ad_typeViewSet, feedbackViewSet,promoted_ad_detailViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('feedback', feedbackViewSet)
router.register('promoted_ad_detail', promoted_ad_detailViewSet)
# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

