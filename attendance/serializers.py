from rest_framework import serializers
from .models import (
    AttendanceActivity, Attendance, AttendanceRequestFile, AttendanceRequestComment,
    AttendanceOverTime, AttendanceLateComeEarlyOut, AttendanceValidationCondition,
    PenaltyAccount, GraceTime, AttendanceGeneralSetting
)


class AttendanceActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceActivity
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class AttendanceRequestFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRequestFile
        fields = '__all__'


class AttendanceRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRequestComment
        fields = '__all__'


class AttendanceOverTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceOverTime
        fields = '__all__'


class AttendanceLateComeEarlyOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLateComeEarlyOut
        fields = '__all__'


class AttendanceValidationConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceValidationCondition
        fields = '__all__'


class PenaltyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenaltyAccount
        fields = '__all__'


class GraceTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraceTime
        fields = '__all__'


class AttendanceGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceGeneralSetting
        fields = '__all__'
