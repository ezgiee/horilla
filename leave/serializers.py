from rest_framework import serializers
from .models import (
    LeaveType, Holiday, CompanyLeave, AvailableLeave, LeaveRequest,
    LeaverequestFile, LeaverequestComment, LeaveAllocationRequest, LeaveallocationrequestComment,
    LeaveRequestConditionApproval, RestrictLeave, CompensatoryLeaveRequest, LeaveGeneralSetting,
    CompensatoryLeaverequestComment
)


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'


class CompanyLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLeave
        fields = '__all__'


class AvailableLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLeave
        fields = '__all__'


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'


class LeaverequestFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaverequestFile
        fields = '__all__'


class LeaverequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaverequestComment
        fields = '__all__'


class LeaveAllocationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveAllocationRequest
        fields = '__all__'


class LeaveallocationrequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveallocationrequestComment
        fields = '__all__'


class LeaveRequestConditionApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequestConditionApproval
        fields = '__all__'


class RestrictLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestrictLeave
        fields = '__all__'


class CompensatoryLeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompensatoryLeaveRequest
        fields = '__all__'


class LeaveGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveGeneralSetting
        fields = '__all__'


class CompensatoryLeaverequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompensatoryLeaverequestComment
        fields = '__all__'
