# views.py
from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    Employee, EmployeeTag, EmployeeWorkInformation, EmployeeBankDetails,
    NoteFiles, EmployeeNote, PolicyMultipleFile, Policy,
    BonusPoint, Actiontype, DisciplinaryAction, EmployeeGeneralSetting
)
from .serializers import (
    EmployeeSerializer, EmployeeTagSerializer, EmployeeWorkInformationSerializer, EmployeeBankDetailsSerializer,
    NoteFilesSerializer, EmployeeNoteSerializer, PolicyMultipleFileSerializer, PolicySerializer,
    BonusPointSerializer, ActiontypeSerializer, DisciplinaryActionSerializer, EmployeeGeneralSettingSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeTagViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTag.objects.all()
    serializer_class = EmployeeTagSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeWorkInformationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeWorkInformation.objects.all()
    serializer_class = EmployeeWorkInformationSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeBankDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeBankDetails.objects.all()
    serializer_class = EmployeeBankDetailsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class NoteFilesViewSet(viewsets.ModelViewSet):
    queryset = NoteFiles.objects.all()
    serializer_class = NoteFilesSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeNoteViewSet(viewsets.ModelViewSet):
    queryset = EmployeeNote.objects.all()
    serializer_class = EmployeeNoteSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class PolicyMultipleFileViewSet(viewsets.ModelViewSet):
    queryset = PolicyMultipleFile.objects.all()
    serializer_class = PolicyMultipleFileSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class BonusPointViewSet(viewsets.ModelViewSet):
    queryset = BonusPoint.objects.all()
    serializer_class = BonusPointSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ActiontypeViewSet(viewsets.ModelViewSet):
    queryset = Actiontype.objects.all()
    serializer_class = ActiontypeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class DisciplinaryActionViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaryAction.objects.all()
    serializer_class = DisciplinaryActionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class EmployeeGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeGeneralSetting.objects.all()
    serializer_class = EmployeeGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
