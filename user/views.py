from .serializers import *
from rest_framework.views import APIView
from rest_framework import serializers, response, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from user.permissions import IsAuthenticatedOrPostOnly


# Create your views here.
class ProfileView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrPostOnly,)

    def get(self, request, format=None):
        username = request.GET.get('username')
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllProfilesView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(UserSerializer(User.objects.all(), many=True).data, status=status.HTTP_200_OK)
