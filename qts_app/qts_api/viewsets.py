from rest_framework import viewsets
from . import models
from . import serailizers


class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class feedbackViewSet(viewsets.ModelViewSet):
    queryset = models.feedback.objects.all()
    serializer_class = serailizers.feedbackSerializer


class promoted_ad_detailViewSet(viewsets.ModelViewSet):
    queryset = models.promoted_ad_detail.objects.all()
    serializer_class = serailizers.promoted_ad_detailSerializer