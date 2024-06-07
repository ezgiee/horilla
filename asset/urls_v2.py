# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    AssetCategoryViewSet, AssetLotViewSet, AssetViewSet,
    AssetReportViewSet, AssetDocumentsViewSet, ReturnImagesViewSet,
    AssetAssignmentViewSet, AssetRequestViewSet
)

router = DefaultRouter()
router.register(r'asset-categories', AssetCategoryViewSet)
router.register(r'asset-lots', AssetLotViewSet)
router.register(r'assets', AssetViewSet)
router.register(r'asset-reports', AssetReportViewSet)
router.register(r'asset-documents', AssetDocumentsViewSet)
router.register(r'return-images', ReturnImagesViewSet)
router.register(r'asset-assignments', AssetAssignmentViewSet)
router.register(r'asset-requests', AssetRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
