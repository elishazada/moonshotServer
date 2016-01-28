import uuid
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_id = models.CharField(max_length=9, primary_key=True)
    question_title = models.CharField(max_length=100)
    question_description = models.CharField(max_length=250)
    user = models.ForeignKey(User, default="Admin")

   
