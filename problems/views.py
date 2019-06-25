from django.shortcuts import render
from .serializers import ProblemsSerializer
from rest_framework.views import APIView
from rest_framework import serializers,response
from . import models

# Create your views here.


class Problems(APIView):
    def get(self,request):
        problems=models.Problem.objects.all()
        serializer=ProblemsSerializer(problems, many=True)
        return response.Response(serializer.data)