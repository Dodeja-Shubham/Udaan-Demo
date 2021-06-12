from django.db import models

# Create your models here.
class Question(models.Model):
    subjective = 'subjective'
    objective = 'objective'
    question_types = (
        ('subjective','subjective'),
        ('objective','objective'),
    )
    question = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255,choices=question_types)
    correct_choice = models.CharField(max_length=255)

    def __str__(self):
        return self.question