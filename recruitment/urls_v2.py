from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    SurveyTemplateViewSet, RecruitmentViewSet, StageViewSet, CandidateViewSet, RejectReasonViewSet,
    RejectedCandidateViewSet, StageFilesViewSet, StageNoteViewSet, RecruitmentSurveyViewSet,
    QuestionOrderingViewSet, RecruitmentSurveyAnswerViewSet, RecruitmentMailTemplateViewSet,
    SkillZoneViewSet, SkillZoneCandidateViewSet, CandidateRatingViewSet, RecruitmentGeneralSettingViewSet,
    InterviewScheduleViewSet
)

router = DefaultRouter()
router.register(r'survey-templates', SurveyTemplateViewSet)
router.register(r'recruitments', RecruitmentViewSet)
router.register(r'stages', StageViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'reject-reasons', RejectReasonViewSet)
router.register(r'rejected-candidates', RejectedCandidateViewSet)
router.register(r'stage-files', StageFilesViewSet)
router.register(r'stage-notes', StageNoteViewSet)
router.register(r'recruitment-surveys', RecruitmentSurveyViewSet)
router.register(r'question-orderings', QuestionOrderingViewSet)
router.register(r'recruitment-survey-answers', RecruitmentSurveyAnswerViewSet)
router.register(r'recruitment-mail-templates', RecruitmentMailTemplateViewSet)
router.register(r'skill-zones', SkillZoneViewSet)
router.register(r'skill-zone-candidates', SkillZoneCandidateViewSet)
router.register(r'candidate-ratings', CandidateRatingViewSet)
router.register(r'recruitment-general-settings', RecruitmentGeneralSettingViewSet)
router.register(r'interview-schedules', InterviewScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
