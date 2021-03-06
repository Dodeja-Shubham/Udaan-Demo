from django.db.models.base import Model
from .models import Answer
from rest_framework import serializers

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"