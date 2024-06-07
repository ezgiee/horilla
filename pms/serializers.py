from rest_framework import serializers
from .models import (
    Period, KeyResult, Objective, EmployeeObjective, Comment, EmployeeKeyResult,
    QuestionTemplate, Question, QuestionOptions, Feedback, AnonymousFeedback, Answer,
    KeyResultFeedback, Meetings, MeetingsAnswer
)


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class KeyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyResult
        fields = '__all__'


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'


class EmployeeObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeObjective
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class EmployeeKeyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeKeyResult
        fields = '__all__'


class QuestionTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTemplate
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOptions
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class AnonymousFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousFeedback
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class KeyResultFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyResultFeedback
        fields = '__all__'


class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = '__all__'


class MeetingsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingsAnswer
        fields = '__all__'
