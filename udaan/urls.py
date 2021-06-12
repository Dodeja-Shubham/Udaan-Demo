from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('rest_auth.registration.urls')),
    path('question/',include('question.urls')),
    path('answer/',include('answers.urls')),
    path('quiz',include('quiz.urls')),
    path('submit_quiz',include('submit_quiz.urls')),
]
