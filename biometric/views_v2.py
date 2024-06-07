# views.py
from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import BiometricDevices, BiometricEmployees, COSECAttendanceArguments
from .serializers import (
    BiometricDevicesSerializer,
    BiometricEmployeesSerializer,
    COSECAttendanceArgumentsSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BiometricDevicesViewSet(viewsets.ModelViewSet):
    queryset = BiometricDevices.objects.all()
    serializer_class = BiometricDevicesSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class BiometricEmployeesViewSet(viewsets.ModelViewSet):
    queryset = BiometricEmployees.objects.all()
    serializer_class = BiometricEmployeesSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class COSECAttendanceArgumentsViewSet(viewsets.ModelViewSet):
    queryset = COSECAttendanceArguments.objects.all()
    serializer_class = COSECAttendanceArgumentsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
