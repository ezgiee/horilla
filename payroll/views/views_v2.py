from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models.models import (
    FilingStatus, Contract, WorkRecord, OverrideAttendance, OverrideLeaveRequest, OverrideWorkInfo,
    MultipleCondition, Allowance, Deduction, Payslip, LoanAccount, ReimbursementMultipleAttachment,
    Reimbursement, ReimbursementFile, ReimbursementrequestComment, PayrollGeneralSetting, EncashmentGeneralSettings
)
from ..serializers import (
    FilingStatusSerializer, ContractSerializer, WorkRecordSerializer, OverrideAttendanceSerializer,
    OverrideLeaveRequestSerializer, OverrideWorkInfoSerializer, MultipleConditionSerializer,
    AllowanceSerializer, DeductionSerializer, PayslipSerializer, LoanAccountSerializer,
    ReimbursementMultipleAttachmentSerializer, ReimbursementSerializer, ReimbursementFileSerializer,
    ReimbursementrequestCommentSerializer, PayrollGeneralSettingSerializer, EncashmentGeneralSettingsSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FilingStatusViewSet(viewsets.ModelViewSet):
    queryset = FilingStatus.objects.all()
    serializer_class = FilingStatusSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class WorkRecordViewSet(viewsets.ModelViewSet):
    queryset = WorkRecord.objects.all()
    serializer_class = WorkRecordSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OverrideAttendanceViewSet(viewsets.ModelViewSet):
    queryset = OverrideAttendance.objects.all()
    serializer_class = OverrideAttendanceSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OverrideLeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = OverrideLeaveRequest.objects.all()
    serializer_class = OverrideLeaveRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OverrideWorkInfoViewSet(viewsets.ModelViewSet):
    queryset = OverrideWorkInfo.objects.all()
    serializer_class = OverrideWorkInfoSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class MultipleConditionViewSet(viewsets.ModelViewSet):
    queryset = MultipleCondition.objects.all()
    serializer_class = MultipleConditionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AllowanceViewSet(viewsets.ModelViewSet):
    queryset = Allowance.objects.all()
    serializer_class = AllowanceSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class DeductionViewSet(viewsets.ModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class PayslipViewSet(viewsets.ModelViewSet):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LoanAccountViewSet(viewsets.ModelViewSet):
    queryset = LoanAccount.objects.all()
    serializer_class = LoanAccountSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ReimbursementMultipleAttachmentViewSet(viewsets.ModelViewSet):
    queryset = ReimbursementMultipleAttachment.objects.all()
    serializer_class = ReimbursementMultipleAttachmentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ReimbursementViewSet(viewsets.ModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ReimbursementFileViewSet(viewsets.ModelViewSet):
    queryset = ReimbursementFile.objects.all()
    serializer_class = ReimbursementFileSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ReimbursementrequestCommentViewSet(viewsets.ModelViewSet):
    queryset = ReimbursementrequestComment.objects.all()
    serializer_class = ReimbursementrequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class PayrollGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = PayrollGeneralSetting.objects.all()
    serializer_class = PayrollGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EncashmentGeneralSettingsViewSet(viewsets.ModelViewSet):
    queryset = EncashmentGeneralSettings.objects.all()
    serializer_class = EncashmentGeneralSettingsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
