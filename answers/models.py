from django.db import models
from question.models import Question
# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return str(self.question)