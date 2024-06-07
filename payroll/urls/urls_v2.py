from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.views_v2 import (
    FilingStatusViewSet, ContractViewSet, WorkRecordViewSet, OverrideAttendanceViewSet, OverrideLeaveRequestViewSet,
    OverrideWorkInfoViewSet, MultipleConditionViewSet, AllowanceViewSet, DeductionViewSet, PayslipViewSet,
    LoanAccountViewSet, ReimbursementMultipleAttachmentViewSet, ReimbursementViewSet, ReimbursementFileViewSet,
    ReimbursementrequestCommentViewSet, PayrollGeneralSettingViewSet, EncashmentGeneralSettingsViewSet
)

router = DefaultRouter()
router.register(r'filingstatuses', FilingStatusViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'workrecords', WorkRecordViewSet)
router.register(r'overrideattendances', OverrideAttendanceViewSet)
router.register(r'overrideleaverequests', OverrideLeaveRequestViewSet)
router.register(r'overrideworkinfos', OverrideWorkInfoViewSet)
router.register(r'multipleconditions', MultipleConditionViewSet)
router.register(r'allowances', AllowanceViewSet)
router.register(r'deductions', DeductionViewSet)
router.register(r'payslips', PayslipViewSet)
router.register(r'loanaccounts', LoanAccountViewSet)
router.register(r'reimbursementmultipleattachments', ReimbursementMultipleAttachmentViewSet)
router.register(r'reimbursements', ReimbursementViewSet)
router.register(r'reimbursementfiles', ReimbursementFileViewSet)
router.register(r'reimbursementrequestcomments', ReimbursementrequestCommentViewSet)
router.register(r'payrollgeneralsettings', PayrollGeneralSettingViewSet)
router.register(r'encashmentgeneralsettings', EncashmentGeneralSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]