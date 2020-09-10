from rest_framework import serializers
from .models import ad_type
from .models import district


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        fields = '__all__'
       # fields = ['type_id', 'type_name']

#District serializer
class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'


