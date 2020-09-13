from qts_api.viewsets import ad_typeViewSet, promotion_packageViewSet,  feedbackViewSet
from qts_api.viewsets import ad_listingViewSet
from qts_api.viewsets import districtViewSet
from qts_api.viewsets import paymentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('promotion_package', promotion_packageViewSet)
router.register('feedback', feedbackViewSet)
router.register('ad_listing', ad_listingViewSet)
router.register('district', districtViewSet)
router.register('payment', paymentViewSet)


# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

