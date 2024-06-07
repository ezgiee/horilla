from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    AttendanceActivityViewSet, AttendanceViewSet, AttendanceRequestFileViewSet,
    AttendanceRequestCommentViewSet, AttendanceOverTimeViewSet, AttendanceLateComeEarlyOutViewSet,
    AttendanceValidationConditionViewSet, PenaltyAccountViewSet, GraceTimeViewSet,
    AttendanceGeneralSettingViewSet
)

router = DefaultRouter()
router.register(r'attendance-activities', AttendanceActivityViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'attendance-request-files', AttendanceRequestFileViewSet)
router.register(r'attendance-request-comments', AttendanceRequestCommentViewSet)
router.register(r'attendance-over-times', AttendanceOverTimeViewSet)
router.register(r'attendance-late-come-early-outs', AttendanceLateComeEarlyOutViewSet)
router.register(r'attendance-validation-conditions', AttendanceValidationConditionViewSet)
router.register(r'penalty-accounts', PenaltyAccountViewSet)
router.register(r'grace-times', GraceTimeViewSet)
router.register(r'attendance-general-settings', AttendanceGeneralSettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
