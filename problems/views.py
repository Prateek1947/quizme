from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . import models
from django.http import JsonResponse
from rest_framework.permissions import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication


# Create your views here.


class ProblemList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        problems = models.Problem.objects.all()
        serializer = ProblemsListSerializer(problems, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProblemsListSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, pk):
        return get_object_or_404(models.Problem, pk=pk)

    def get(self, request, pk):
        prob = self.get_object(pk)
        self.check_object_permissions(request, prob)
        serializer = ProblemDetailSerializer(prob)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        prob = self.get_object(pk)
        self.check_object_permissions(request, prob)
        serializer = ProblemDetailSerializer(prob, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prob = self.get_object(pk)
        self.check_object_permissions(request, prob)
        prob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        user.auth_token.delete()
        return JsonResponse({'detail': "user logged out"}, status=status.HTTP_200_OK)
