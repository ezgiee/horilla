from rest_framework import serializers
from .models import Offboarding, OffboardingStage, OffboardingStageMultipleFile, OffboardingEmployee, ResignationLetter, OffboardingTask, EmployeeTask, ExitReason, OffboardingNote, OffboardingGeneralSetting


class OffboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offboarding
        fields = '__all__'


class OffboardingStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingStage
        fields = '__all__'


class OffboardingStageMultipleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingStageMultipleFile
        fields = '__all__'


class OffboardingEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingEmployee
        fields = '__all__'


class ResignationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResignationLetter
        fields = '__all__'


class OffboardingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingTask
        fields = '__all__'


class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTask
        fields = '__all__'


class ExitReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitReason
        fields = '__all__'


class OffboardingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingNote
        fields = '__all__'


class OffboardingGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingGeneralSetting
        fields = '__all__'
