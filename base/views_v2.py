from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    Company, Department, JobPosition, JobRole, WorkType, RotatingWorkType,
    RotatingWorkTypeAssign, EmployeeType, EmployeeShift, EmployeeShiftSchedule, RotatingShift,
    RotatingShiftAssign, WorkTypeRequest, WorkTypeRequestComment, ShiftRequest, ShiftRequestComment,
    Tags, DynamicEmailConfiguration, MultipleApprovalCondition, Announcement,
    AnnouncementComment, DashboardEmployeeCharts
)
from .serializers import (
    CompanySerializer, DepartmentSerializer, JobPositionSerializer, JobRoleSerializer, WorkTypeSerializer, RotatingWorkTypeSerializer, RotatingWorkTypeAssignSerializer,
    EmployeeTypeSerializer, EmployeeShiftSerializer, EmployeeShiftScheduleSerializer,
    RotatingShiftSerializer, RotatingShiftAssignSerializer, WorkTypeRequestSerializer,
    WorkTypeRequestCommentSerializer, ShiftRequestSerializer, ShiftRequestCommentSerializer,
    TagsSerializer, DynamicEmailConfigurationSerializer, MultipleApprovalConditionSerializer,
    AnnouncementSerializer, AnnouncementCommentSerializer, DashboardEmployeeChartsSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class JobRoleViewSet(viewsets.ModelViewSet):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class RotatingWorkTypeViewSet(viewsets.ModelViewSet):
    queryset = RotatingWorkType.objects.all()
    serializer_class = RotatingWorkTypeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class RotatingWorkTypeAssignViewSet(viewsets.ModelViewSet):
    queryset = RotatingWorkTypeAssign.objects.all()
    serializer_class = RotatingWorkTypeAssignSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class EmployeeShiftViewSet(viewsets.ModelViewSet):
    queryset = EmployeeShift.objects.all()
    serializer_class = EmployeeShiftSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class EmployeeShiftScheduleViewSet(viewsets.ModelViewSet):
    queryset = EmployeeShiftSchedule.objects.all()
    serializer_class = EmployeeShiftScheduleSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class RotatingShiftViewSet(viewsets.ModelViewSet):
    queryset = RotatingShift.objects.all()
    serializer_class = RotatingShiftSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class RotatingShiftAssignViewSet(viewsets.ModelViewSet):
    queryset = RotatingShiftAssign.objects.all()
    serializer_class = RotatingShiftAssignSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class WorkTypeRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkTypeRequest.objects.all()
    serializer_class = WorkTypeRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class WorkTypeRequestCommentViewSet(viewsets.ModelViewSet):
    queryset = WorkTypeRequestComment.objects.all()
    serializer_class = WorkTypeRequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class ShiftRequestViewSet(viewsets.ModelViewSet):
    queryset = ShiftRequest.objects.all()
    serializer_class = ShiftRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class ShiftRequestCommentViewSet(viewsets.ModelViewSet):
    queryset = ShiftRequestComment.objects.all()
    serializer_class = ShiftRequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class DynamicEmailConfigurationViewSet(viewsets.ModelViewSet):
    queryset = DynamicEmailConfiguration.objects.all()
    serializer_class = DynamicEmailConfigurationSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class MultipleApprovalConditionViewSet(viewsets.ModelViewSet):
    queryset = MultipleApprovalCondition.objects.all()
    serializer_class = MultipleApprovalConditionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class AnnouncementCommentViewSet(viewsets.ModelViewSet):
    queryset = AnnouncementComment.objects.all()
    serializer_class = AnnouncementCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

class DashboardEmployeeChartsViewSet(viewsets.ModelViewSet):
    queryset = DashboardEmployeeCharts.objects.all()
    serializer_class = DashboardEmployeeChartsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

