# serializers.py
from rest_framework import serializers
from .models import (
    Employee, EmployeeTag, EmployeeWorkInformation, EmployeeBankDetails,
    NoteFiles, EmployeeNote, PolicyMultipleFile, Policy,
    BonusPoint, Actiontype, DisciplinaryAction, EmployeeGeneralSetting
)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTag
        fields = '__all__'


class EmployeeWorkInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkInformation
        fields = '__all__'


class EmployeeBankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBankDetails
        fields = '__all__'


class NoteFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteFiles
        fields = '__all__'


class EmployeeNoteSerializer(serializers.ModelSerializer):
    files = NoteFilesSerializer(many=True, read_only=True)

    class Meta:
        model = EmployeeNote
        fields = '__all__'


class PolicyMultipleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyMultipleFile
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    files = PolicyMultipleFileSerializer(many=True, read_only=True)

    class Meta:
        model = Policy
        fields = '__all__'


class BonusPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusPoint
        fields = '__all__'


class ActiontypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actiontype
        fields = '__all__'


class DisciplinaryActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaryAction
        fields = '__all__'


class EmployeeGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGeneralSetting
        fields = '__all__'
