from rest_framework import serializers
from .models import (
    Company, Department, JobPosition, JobRole, WorkType, RotatingWorkType, RotatingWorkTypeAssign, EmployeeType,
    EmployeeShift, EmployeeShiftSchedule, RotatingShift, RotatingShiftAssign,
    WorkTypeRequest, WorkTypeRequestComment, ShiftRequest, ShiftRequestComment,
    Tags, DynamicEmailConfiguration, MultipleApprovalCondition, Announcement,
    AnnouncementComment, DashboardEmployeeCharts
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = '__all__'


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'


class RotatingWorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotatingWorkType
        fields = '__all__'


class RotatingWorkTypeAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotatingWorkTypeAssign
        fields = '__all__'


class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = '__all__'


class EmployeeShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeShift
        fields = '__all__'


class EmployeeShiftScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeShiftSchedule
        fields = '__all__'


class RotatingShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotatingShift
        fields = '__all__'


class RotatingShiftAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotatingShiftAssign
        fields = '__all__'


class WorkTypeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTypeRequest
        fields = '__all__'


class WorkTypeRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTypeRequestComment
        fields = '__all__'


class ShiftRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftRequest
        fields = '__all__'


class ShiftRequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftRequestComment
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class DynamicEmailConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicEmailConfiguration
        fields = '__all__'


class MultipleApprovalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleApprovalCondition
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementComment
        fields = '__all__'


class DashboardEmployeeChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardEmployeeCharts
        fields = '__all__'
