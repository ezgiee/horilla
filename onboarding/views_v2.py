from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import OnboardingStage, OnboardingTask, CandidateStage, CandidateTask, OnboardingPortal
from .serializers import OnboardingStageSerializer, OnboardingTaskSerializer, CandidateStageSerializer, CandidateTaskSerializer, OnboardingPortalSerializer


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class OnboardingStageViewSet(viewsets.ModelViewSet):
    queryset = OnboardingStage.objects.all()
    serializer_class = OnboardingStageSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OnboardingTaskViewSet(viewsets.ModelViewSet):
    queryset = OnboardingTask.objects.all()
    serializer_class = OnboardingTaskSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CandidateStageViewSet(viewsets.ModelViewSet):
    queryset = CandidateStage.objects.all()
    serializer_class = CandidateStageSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CandidateTaskViewSet(viewsets.ModelViewSet):
    queryset = CandidateTask.objects.all()
    serializer_class = CandidateTaskSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class OnboardingPortalViewSet(viewsets.ModelViewSet):
    queryset = OnboardingPortal.objects.all()
    serializer_class = OnboardingPortalSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
