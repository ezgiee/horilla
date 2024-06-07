from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views_v2 import (
    CompanyViewSet, DepartmentViewSet, JobPositionViewSet, JobRoleViewSet, WorkTypeViewSet, RotatingWorkTypeViewSet, RotatingWorkTypeAssignViewSet,
    EmployeeTypeViewSet, EmployeeShiftViewSet, EmployeeShiftScheduleViewSet,
    RotatingShiftViewSet, RotatingShiftAssignViewSet, WorkTypeRequestViewSet,
    WorkTypeRequestCommentViewSet, ShiftRequestViewSet, ShiftRequestCommentViewSet,
    TagsViewSet, DynamicEmailConfigurationViewSet, MultipleApprovalConditionViewSet,
    AnnouncementViewSet, AnnouncementCommentViewSet, DashboardEmployeeChartsViewSet
)


router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'jobposition', JobPositionViewSet)
router.register(r'jobrole', JobRoleViewSet)
router.register(r'worktypes', WorkTypeViewSet)
router.register(r'rotatingworktypes', RotatingWorkTypeViewSet)
router.register(r'rotatingworktypeassigns', RotatingWorkTypeAssignViewSet)
router.register(r'employeetypes', EmployeeTypeViewSet)
router.register(r'employeeshifts', EmployeeShiftViewSet)
router.register(r'employeeshiftschedules', EmployeeShiftScheduleViewSet)
router.register(r'rotatingshifts', RotatingShiftViewSet)
router.register(r'rotatingshiftassigns', RotatingShiftAssignViewSet)
router.register(r'worktyperequests', WorkTypeRequestViewSet)
router.register(r'worktyperequestcomments', WorkTypeRequestCommentViewSet)
router.register(r'shiftrequests', ShiftRequestViewSet)
router.register(r'shiftrequestcomments', ShiftRequestCommentViewSet)
router.register(r'tags', TagsViewSet)
router.register(r'dynamicemailconfigurations', DynamicEmailConfigurationViewSet)
router.register(r'multipleapprovalconditions', MultipleApprovalConditionViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'announcementcomments', AnnouncementCommentViewSet)
router.register(r'dashboardemployeecharts', DashboardEmployeeChartsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]