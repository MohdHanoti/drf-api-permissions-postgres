from rest_framework import serializers

from .models import Electric,Electronics
class ElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model= Electric
        fields='__all__'


class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Electronics
        fields='__all__'