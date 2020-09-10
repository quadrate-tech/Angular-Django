from rest_framework import serializers
from .models import ad_type, payment


class ad_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad_type
        # fields = '__all__'
        fields = ['type_id', 'type_name']
class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'

