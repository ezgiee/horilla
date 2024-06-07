from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import OffboardingViewSet, OffboardingStageViewSet, OffboardingStageMultipleFileViewSet, OffboardingEmployeeViewSet, ResignationLetterViewSet, OffboardingTaskViewSet, EmployeeTaskViewSet, ExitReasonViewSet, OffboardingNoteViewSet, OffboardingGeneralSettingViewSet

router = DefaultRouter()
router.register(r'offboardings', OffboardingViewSet)
router.register(r'offboardingstages', OffboardingStageViewSet)
router.register(r'offboardingstagemultiplefiles', OffboardingStageMultipleFileViewSet)
router.register(r'offboardingemployees', OffboardingEmployeeViewSet)
router.register(r'resignationletters', ResignationLetterViewSet)
router.register(r'offboardingtasks', OffboardingTaskViewSet)
router.register(r'employeetasks', EmployeeTaskViewSet)
router.register(r'exitreasons', ExitReasonViewSet)
router.register(r'offboardingnotes', OffboardingNoteViewSet)
router.register(r'offboardinggeneralsettings', OffboardingGeneralSettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
