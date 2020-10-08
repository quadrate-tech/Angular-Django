from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models, serailizers


class parent_categoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.parent_category.objects.all()
    serializer_class = serailizers.parent_categorySerializer


class sub_categoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.sub_category.objects.all()
    serializer_class = serailizers.sub_categorySerializer


class ad_listingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.ad_listing.objects.all()
    serializer_class = serailizers.ad_listingSerializer

    
class ad_typeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class feedbackViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.feedback.objects.all()
    serializer_class = serailizers.feedbackSerializer


class districtViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.district.objects.all()
    serializer_class = serailizers.districtSerializer


class cityViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.city.objects.all()
    serializer_class = serailizers.citySerializer


class imageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.image.objects.all()
    serializer_class = serailizers.imageSeralizer

    
class userViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.user.objects.all()
    serializer_class = serailizers.userSerializer


class promoted_ad_detailViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.promoted_ad_detail.objects.all()
    serializer_class = serailizers.promoted_ad_detail


class promotion_packageViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.promotion_package.objects.all()
    serializer_class = serailizers.promotion_packageSerializer


class paymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.payment.objects.all()
    serializer_class = serailizers.paymentSerializer
