# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import BiometricDevicesViewSet, BiometricEmployeesViewSet, COSECAttendanceArgumentsViewSet

router = DefaultRouter()
router.register(r'biometricdevices', BiometricDevicesViewSet)
router.register(r'biometricemployees', BiometricEmployeesViewSet)
router.register(r'cosecattendancearguments', COSECAttendanceArgumentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
