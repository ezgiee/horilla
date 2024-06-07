from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Offboarding, OffboardingStage, OffboardingStageMultipleFile, OffboardingEmployee, ResignationLetter, OffboardingTask, EmployeeTask, ExitReason, OffboardingNote, OffboardingGeneralSetting
from .serializers import OffboardingSerializer, OffboardingStageSerializer, OffboardingStageMultipleFileSerializer, OffboardingEmployeeSerializer, ResignationLetterSerializer, OffboardingTaskSerializer, EmployeeTaskSerializer, ExitReasonSerializer, OffboardingNoteSerializer, OffboardingGeneralSettingSerializer


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class OffboardingViewSet(viewsets.ModelViewSet):
    queryset = Offboarding.objects.all()
    serializer_class = OffboardingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingStageViewSet(viewsets.ModelViewSet):
    queryset = OffboardingStage.objects.all()
    serializer_class = OffboardingStageSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingStageMultipleFileViewSet(viewsets.ModelViewSet):
    queryset = OffboardingStageMultipleFile.objects.all()
    serializer_class = OffboardingStageMultipleFileSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingEmployeeViewSet(viewsets.ModelViewSet):
    queryset = OffboardingEmployee.objects.all()
    serializer_class = OffboardingEmployeeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ResignationLetterViewSet(viewsets.ModelViewSet):
    queryset = ResignationLetter.objects.all()
    serializer_class = ResignationLetterSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingTaskViewSet(viewsets.ModelViewSet):
    queryset = OffboardingTask.objects.all()
    serializer_class = OffboardingTaskSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeTaskViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTask.objects.all()
    serializer_class = EmployeeTaskSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ExitReasonViewSet(viewsets.ModelViewSet):
    queryset = ExitReason.objects.all()
    serializer_class = ExitReasonSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingNoteViewSet(viewsets.ModelViewSet):
    queryset = OffboardingNote.objects.all()
    serializer_class = OffboardingNoteSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OffboardingGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = OffboardingGeneralSetting.objects.all()
    serializer_class = OffboardingGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
