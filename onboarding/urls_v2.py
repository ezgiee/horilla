from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import OnboardingStageViewSet, OnboardingTaskViewSet, CandidateStageViewSet, CandidateTaskViewSet, OnboardingPortalViewSet

router = DefaultRouter()
router.register(r'onboardingstages', OnboardingStageViewSet)
router.register(r'onboardingtasks', OnboardingTaskViewSet)
router.register(r'candidatestages', CandidateStageViewSet)
router.register(r'candidatetasks', CandidateTaskViewSet)
router.register(r'onboardingportals', OnboardingPortalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
