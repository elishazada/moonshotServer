from rest_framework import serializers
from .models import Question
from django.contrib.auth.models import User
import uuid



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'question_title', 'question_description', 'user')