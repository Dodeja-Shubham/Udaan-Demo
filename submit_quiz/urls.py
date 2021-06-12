from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Submit_QuizView.as_view(),name="Submit_Quiz List and Create API"),
]
