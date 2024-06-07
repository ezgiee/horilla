from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    LeaveTypeViewSet, HolidayViewSet, CompanyLeaveViewSet, AvailableLeaveViewSet,
    LeaveRequestViewSet, LeaverequestFileViewSet, LeaverequestCommentViewSet,
    LeaveAllocationRequestViewSet, LeaveallocationrequestCommentViewSet, LeaveRequestConditionApprovalViewSet,
    RestrictLeaveViewSet, CompensatoryLeaveRequestViewSet, LeaveGeneralSettingViewSet,
    CompensatoryLeaverequestCommentViewSet
)

router = DefaultRouter()
router.register(r'leavetypes', LeaveTypeViewSet)
router.register(r'holidays', HolidayViewSet)
router.register(r'companyleaves', CompanyLeaveViewSet)
router.register(r'availableleaves', AvailableLeaveViewSet)
router.register(r'leaverequests', LeaveRequestViewSet)
router.register(r'leaverequestfiles', LeaverequestFileViewSet)
router.register(r'leaverequestcomments', LeaverequestCommentViewSet)
router.register(r'leaveallocationrequests', LeaveAllocationRequestViewSet)
router.register(r'leaveallocationrequestcomments', LeaveallocationrequestCommentViewSet)
router.register(r'leaverequestconditionapprovals', LeaveRequestConditionApprovalViewSet)
router.register(r'restrictleaves', RestrictLeaveViewSet)
router.register(r'compensatoryleaverequests', CompensatoryLeaveRequestViewSet)
router.register(r'leavegeneralsettings', LeaveGeneralSettingViewSet)
router.register(r'compensatoryleaverequestcomments', CompensatoryLeaverequestCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
