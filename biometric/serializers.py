from rest_framework import serializers
from .models import BiometricDevices, BiometricEmployees, COSECAttendanceArguments


class BiometricDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricDevices
        fields = '__all__'


class BiometricEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricEmployees
        fields = '__all__'


class COSECAttendanceArgumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = COSECAttendanceArguments
        fields = '__all__'
