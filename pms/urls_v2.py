from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    PeriodViewSet, KeyResultViewSet, ObjectiveViewSet, EmployeeObjectiveViewSet,
    CommentViewSet, EmployeeKeyResultViewSet, QuestionTemplateViewSet, QuestionViewSet,
    QuestionOptionsViewSet, FeedbackViewSet, AnonymousFeedbackViewSet, AnswerViewSet,
    KeyResultFeedbackViewSet, MeetingsViewSet, MeetingsAnswerViewSet
)

router = DefaultRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'key-results', KeyResultViewSet)
router.register(r'objectives', ObjectiveViewSet)
router.register(r'employee-objectives', EmployeeObjectiveViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'employee-key-results', EmployeeKeyResultViewSet)
router.register(r'question-templates', QuestionTemplateViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'question-options', QuestionOptionsViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'anonymous-feedbacks', AnonymousFeedbackViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'key-result-feedbacks', KeyResultFeedbackViewSet)
router.register(r'meetings', MeetingsViewSet)
router.register(r'meetings-answers', MeetingsAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
