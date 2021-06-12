from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuestionView.as_view(),name="Questions List and Create API"),
]
