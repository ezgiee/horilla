from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    AttendanceActivity, Attendance, AttendanceRequestFile, AttendanceRequestComment,
    AttendanceOverTime, AttendanceLateComeEarlyOut, AttendanceValidationCondition,
    PenaltyAccount, GraceTime, AttendanceGeneralSetting
)
from .serializers import (
    AttendanceActivitySerializer, AttendanceSerializer, AttendanceRequestFileSerializer,
    AttendanceRequestCommentSerializer, AttendanceOverTimeSerializer, AttendanceLateComeEarlyOutSerializer,
    AttendanceValidationConditionSerializer, PenaltyAccountSerializer, GraceTimeSerializer,
    AttendanceGeneralSettingSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AttendanceActivityViewSet(viewsets.ModelViewSet):
    queryset = AttendanceActivity.objects.all()
    serializer_class = AttendanceActivitySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceRequestFileViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRequestFile.objects.all()
    serializer_class = AttendanceRequestFileSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceRequestCommentViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRequestComment.objects.all()
    serializer_class = AttendanceRequestCommentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceOverTimeViewSet(viewsets.ModelViewSet):
    queryset = AttendanceOverTime.objects.all()
    serializer_class = AttendanceOverTimeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceLateComeEarlyOutViewSet(viewsets.ModelViewSet):
    queryset = AttendanceLateComeEarlyOut.objects.all()
    serializer_class = AttendanceLateComeEarlyOutSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceValidationConditionViewSet(viewsets.ModelViewSet):
    queryset = AttendanceValidationCondition.objects.all()
    serializer_class = AttendanceValidationConditionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class PenaltyAccountViewSet(viewsets.ModelViewSet):
    queryset = PenaltyAccount.objects.all()
    serializer_class = PenaltyAccountSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class GraceTimeViewSet(viewsets.ModelViewSet):
    queryset = GraceTime.objects.all()
    serializer_class = GraceTimeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AttendanceGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = AttendanceGeneralSetting.objects.all()
    serializer_class = AttendanceGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
