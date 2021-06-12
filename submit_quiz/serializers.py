from django.db.models.base import Model
from .models import Submit_Quiz
from rest_framework import serializers

class Submit_QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit_Quiz
        fields = "__all__"