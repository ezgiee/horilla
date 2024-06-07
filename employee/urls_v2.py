# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    EmployeeViewSet, EmployeeTagViewSet, EmployeeWorkInformationViewSet, EmployeeBankDetailsViewSet,
    NoteFilesViewSet, EmployeeNoteViewSet, PolicyMultipleFileViewSet, PolicyViewSet,
    BonusPointViewSet, ActiontypeViewSet, DisciplinaryActionViewSet, EmployeeGeneralSettingViewSet
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'employee-tags', EmployeeTagViewSet)
router.register(r'employee-work-information', EmployeeWorkInformationViewSet)
router.register(r'employee-bank-details', EmployeeBankDetailsViewSet)
router.register(r'note-files', NoteFilesViewSet)
router.register(r'employee-notes', EmployeeNoteViewSet)
router.register(r'policy-multiple-files', PolicyMultipleFileViewSet)
router.register(r'policies', PolicyViewSet)
router.register(r'bonus-points', BonusPointViewSet)
router.register(r'action-types', ActiontypeViewSet)
router.register(r'disciplinary-actions', DisciplinaryActionViewSet)
router.register(r'employee-general-settings', EmployeeGeneralSettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
