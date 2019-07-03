from rest_framework.views import APIView
from .serializers import SubmissionSerializer
from .models import Submission
from rest_framework.response import Response
from rest_framework.status import *
from user.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404


# Create your views here.

class ActivityView(APIView):
    def get(self, request, format=None):
        serializer = SubmissionSerializer(Submission.objects.all(), many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class SubmissionView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        user = get_object_or_404(User, username=request.GET.get('username'))
        serializer = SubmissionSerializer(user.submission_set.all(), many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
