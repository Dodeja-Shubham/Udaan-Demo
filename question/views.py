from django.shortcuts import render
from rest_framework import generics,mixins,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer
from answers.models import Answer
from answers.serializers import AnswerSerializer
# Create your views here.

class QuestionView(generics.ListCreateAPIView):
    model = Question
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request):
        context = self.get_queryset()
        serializer = self.serializer_class(context,many=True)
        try:
            # res = []
            # for data in serializer.data:
            #     answer_choices = Answer.objects.filter(question=data['id'])
            #     serailized_answer = AnswerSerializer(answer_choices)
            #     data['answers'] = serailized_answer.data
            #     res.append(data)
            #     print(data)
            # return Response(serializer.data,status=status.HTTP_200_OK)
            return self.list(request)
        except Exception as e:
            return Response(str(e))
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)