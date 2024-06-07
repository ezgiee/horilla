from rest_framework import serializers
from .models import (
    SurveyTemplate, Recruitment, Stage, Candidate, RejectReason, RejectedCandidate,
    StageFiles, StageNote, RecruitmentSurvey, QuestionOrdering, RecruitmentSurveyAnswer,
    RecruitmentMailTemplate, SkillZone, SkillZoneCandidate, CandidateRating, RecruitmentGeneralSetting,
    InterviewSchedule
)


class SurveyTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyTemplate
        fields = '__all__'


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class RejectReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectReason
        fields = '__all__'


class RejectedCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectedCandidate
        fields = '__all__'


class StageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageFiles
        fields = '__all__'


class StageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageNote
        fields = '__all__'


class RecruitmentSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentSurvey
        fields = '__all__'


class QuestionOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOrdering
        fields = '__all__'


class RecruitmentSurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentSurveyAnswer
        fields = '__all__'


class RecruitmentMailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentMailTemplate
        fields = '__all__'


class SkillZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillZone
        fields = '__all__'


class SkillZoneCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillZoneCandidate
        fields = '__all__'


class CandidateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRating
        fields = '__all__'


class RecruitmentGeneralSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentGeneralSetting
        fields = '__all__'


class InterviewScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSchedule
        fields = '__all__'
