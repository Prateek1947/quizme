from .serializers import *
from rest_framework.views import APIView
from rest_framework import serializers, response, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class ProfileView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
