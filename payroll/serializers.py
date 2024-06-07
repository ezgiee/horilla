from rest_framework import serializers
from .models.models import (
    FilingStatus, Contract, WorkRecord, OverrideAttendance, OverrideLeaveRequest, OverrideWorkInfo,
    MultipleCondition, Allowance, Deduction, Payslip, LoanAccount, ReimbursementMultipleAttachment,
    Reimbursement, ReimbursementFile, ReimbursementrequestComment, PayrollGeneralSetting, EncashmentGeneralSettings
)


class FilingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilingStatus
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class WorkRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRecord
        fields = '__all__'


class OverrideAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverrideAttendance
        fields = '__all__'


class OverrideLeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverrideLeaveRequest
        fields = '__all__'


class OverrideWorkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverrideWorkInfo
        fields = '__all__'


class MultipleConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleCondition
        fields = '__all__'


class AllowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allowance
        fields = '__all__'


class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = '__all__'


class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'


class LoanAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAccount
        fields = '__all__'


class ReimbursementMultipleAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReimbursementMultipleAttachment
        fields = '__all__'


class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = '__all__'


class ReimbursementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReimbursementFile
        fields = '__all__'


class ReimbursementrequestCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReimbursementrequestComment
        fields = '__all__'


class PayrollGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollGeneralSetting
        fields = '__all__'


class EncashmentGeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncashmentGeneralSettings
        fields = '__all__'
