from rest_framework import viewsets
from . import models
from . import serailizers



class ad_typeViewSet(viewsets.ModelViewSet):
    queryset = models.ad_type.objects.all()
    serializer_class = serailizers.ad_typeSerializer


class districtViewSet(viewsets.ModelViewSet):
    queryset = models.district.objects.all()
    serializer_class = serailizers.districtSerializer