# views.py
from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    AssetCategory, AssetLot, Asset, AssetReport, AssetDocuments,
    ReturnImages, AssetAssignment, AssetRequest
)
from .serializers import (
    AssetCategorySerializer, AssetLotSerializer, AssetSerializer,
    AssetReportSerializer, AssetDocumentsSerializer, ReturnImagesSerializer,
    AssetAssignmentSerializer, AssetRequestSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetLotViewSet(viewsets.ModelViewSet):
    queryset = AssetLot.objects.all()
    serializer_class = AssetLotSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetReportViewSet(viewsets.ModelViewSet):
    queryset = AssetReport.objects.all()
    serializer_class = AssetReportSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetDocumentsViewSet(viewsets.ModelViewSet):
    queryset = AssetDocuments.objects.all()
    serializer_class = AssetDocumentsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class ReturnImagesViewSet(viewsets.ModelViewSet):
    queryset = ReturnImages.objects.all()
    serializer_class = ReturnImagesSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetAssignmentViewSet(viewsets.ModelViewSet):
    queryset = AssetAssignment.objects.all()
    serializer_class = AssetAssignmentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class AssetRequestViewSet(viewsets.ModelViewSet):
    queryset = AssetRequest.objects.all()
    serializer_class = AssetRequestSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
