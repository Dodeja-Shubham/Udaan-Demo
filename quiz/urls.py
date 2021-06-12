from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuizView.as_view(),name="Quiz List and Create API"),
]
