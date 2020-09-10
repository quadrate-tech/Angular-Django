from rest_framework import serializers
from .models import ad_type
from .models import feedback
from .models import promoted_ad_detail

class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        fields = '__all__'


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'


class promoted_ad_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = promoted_ad_detail
        fields = '__all__'