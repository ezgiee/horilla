from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    LeaveType, Holiday, CompanyLeave, AvailableLeave, LeaveRequest,
    LeaverequestFile, LeaverequestComment, LeaveAllocationRequest, LeaveallocationrequestComment,
    LeaveRequestConditionApproval, RestrictLeave, CompensatoryLeaveRequest, LeaveGeneralSetting,
    CompensatoryLeaverequestComment
)
from .serializers import (
    LeaveTypeSerializer, HolidaySerializer, CompanyLeaveSerializer, AvailableLeaveSerializer,
    LeaveRequestSerializer, LeaverequestFileSerializer, LeaverequestCommentSerializer,
    LeaveAllocationRequestSerializer, LeaveallocationrequestCommentSerializer,
    LeaveRequestConditionApprovalSerializer, RestrictLeaveSerializer, CompensatoryLeaveRequestSerializer,
    LeaveGeneralSettingSerializer, CompensatoryLeaverequestCommentSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CompanyLeaveViewSet(viewsets.ModelViewSet):
    queryset = CompanyLeave.objects.all()
    serializer_class = CompanyLeaveSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AvailableLeaveViewSet(viewsets.ModelViewSet):
    queryset = AvailableLeave.objects.all()
    serializer_class = AvailableLeaveSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaverequestFileViewSet(viewsets.ModelViewSet):
    queryset = LeaverequestFile.objects.all()
    serializer_class = LeaverequestFileSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaverequestCommentViewSet(viewsets.ModelViewSet):
    queryset = LeaverequestComment.objects.all()
    serializer_class = LeaverequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaveAllocationRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveAllocationRequest.objects.all()
    serializer_class = LeaveAllocationRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaveallocationrequestCommentViewSet(viewsets.ModelViewSet):
    queryset = LeaveallocationrequestComment.objects.all()
    serializer_class = LeaveallocationrequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaveRequestConditionApprovalViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequestConditionApproval.objects.all()
    serializer_class = LeaveRequestConditionApprovalSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RestrictLeaveViewSet(viewsets.ModelViewSet):
    queryset = RestrictLeave.objects.all()
    serializer_class = RestrictLeaveSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CompensatoryLeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = CompensatoryLeaveRequest.objects.all()
    serializer_class = CompensatoryLeaveRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class LeaveGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = LeaveGeneralSetting.objects.all()
    serializer_class = LeaveGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CompensatoryLeaverequestCommentViewSet(viewsets.ModelViewSet):
    queryset = CompensatoryLeaverequestComment.objects.all()
    serializer_class = CompensatoryLeaverequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
