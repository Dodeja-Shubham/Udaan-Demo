from django.db import models
from question.models import Question
# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return str(self.name)