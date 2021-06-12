from django.shortcuts import render
from rest_framework import generics,mixins,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Answer
from .serializers import AnswerSerializer
# Create your views here.

class AnswerView(APIView):
    model = Answer
    serializer_class = AnswerSerializer

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
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Answer_choices_to_Question(APIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self,request,id=None):
        if id:
            context = self.get_queryset().filter(question=id)
            serializer = self.serializer_class(context,many=True)
            try:
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e))