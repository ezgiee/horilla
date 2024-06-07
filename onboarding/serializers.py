from rest_framework import serializers
from .models import OnboardingStage, OnboardingTask, CandidateStage, CandidateTask, OnboardingPortal


class OnboardingStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingStage
        fields = '__all__'


class OnboardingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingTask
        fields = '__all__'


class CandidateStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateStage
        fields = '__all__'


class CandidateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTask
        fields = '__all__'


class OnboardingPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingPortal
        fields = '__all__'
