from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AnswerView.as_view(),name="Answers List and Create API"),
    path('question/<int:id>', views.Answer_choices_to_Question.as_view(),name="Answers List and Create API"),
]
