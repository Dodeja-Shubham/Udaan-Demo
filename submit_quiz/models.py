from django.db import models
from quiz.models import Quiz
from question.models import Question
# Create your models here.

class Submit_Quiz(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(blank=True,null = True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.answer)
