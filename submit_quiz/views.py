from django.shortcuts import render
from rest_framework import generics,mixins,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Submit_Quiz
from .serializers import Submit_QuizSerializer
from question.models import Question
from quiz.models import Quiz
# Create your views here.

class Submit_QuizView(APIView):
    model = Submit_Quiz
    serializer_class = Submit_QuizSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request):
        context = self.get_queryset()
        serializer = self.serializer_class(context,many=True)
        try:
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            quiz_answer = serializer.save()
            correct_answer = Question.objects.filter(question=serializer.validated_data.get('question')).values_list('correct_choice',flat=True)[0]
            answer = serializer.validated_data.get('answer')
            print(correct_answer,answer)
            if correct_answer == answer:
                quiz_answer.is_correct = True
                quiz_answer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)