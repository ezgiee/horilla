from rest_framework import viewsets, pagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    SurveyTemplate, Recruitment, Stage, Candidate, RejectReason, RejectedCandidate,
    StageFiles, StageNote, RecruitmentSurvey, QuestionOrdering, RecruitmentSurveyAnswer,
    RecruitmentMailTemplate, SkillZone, SkillZoneCandidate, CandidateRating, RecruitmentGeneralSetting,
    InterviewSchedule
)
from .serializers import (
    SurveyTemplateSerializer, RecruitmentSerializer, StageSerializer, CandidateSerializer, RejectReasonSerializer,
    RejectedCandidateSerializer, StageFilesSerializer, StageNoteSerializer, RecruitmentSurveySerializer,
    QuestionOrderingSerializer, RecruitmentSurveyAnswerSerializer, RecruitmentMailTemplateSerializer,
    SkillZoneSerializer, SkillZoneCandidateSerializer, CandidateRatingSerializer, RecruitmentGeneralSettingSerializer,
    InterviewScheduleSerializer
)


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class SurveyTemplateViewSet(viewsets.ModelViewSet):
    queryset = SurveyTemplate.objects.all()
    serializer_class = SurveyTemplateSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RejectReasonViewSet(viewsets.ModelViewSet):
    queryset = RejectReason.objects.all()
    serializer_class = RejectReasonSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RejectedCandidateViewSet(viewsets.ModelViewSet):
    queryset = RejectedCandidate.objects.all()
    serializer_class = RejectedCandidateSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class StageFilesViewSet(viewsets.ModelViewSet):
    queryset = StageFiles.objects.all()
    serializer_class = StageFilesSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class StageNoteViewSet(viewsets.ModelViewSet):
    queryset = StageNote.objects.all()
    serializer_class = StageNoteSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RecruitmentSurveyViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentSurvey.objects.all()
    serializer_class = RecruitmentSurveySerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class QuestionOrderingViewSet(viewsets.ModelViewSet):
    queryset = QuestionOrdering.objects.all()
    serializer_class = QuestionOrderingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RecruitmentSurveyAnswerViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentSurveyAnswer.objects.all()
    serializer_class = RecruitmentSurveyAnswerSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RecruitmentMailTemplateViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentMailTemplate.objects.all()
    serializer_class = RecruitmentMailTemplateSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class SkillZoneViewSet(viewsets.ModelViewSet):
    queryset = SkillZone.objects.all()
    serializer_class = SkillZoneSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class SkillZoneCandidateViewSet(viewsets.ModelViewSet):
    queryset = SkillZoneCandidate.objects.all()
    serializer_class = SkillZoneCandidateSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class CandidateRatingViewSet(viewsets.ModelViewSet):
    queryset = CandidateRating.objects.all()
    serializer_class = CandidateRatingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class RecruitmentGeneralSettingViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentGeneralSetting.objects.all()
    serializer_class = RecruitmentGeneralSettingSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination


class InterviewScheduleViewSet(viewsets.ModelViewSet):
    queryset = InterviewSchedule.objects.all()
    serializer_class = InterviewScheduleSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
