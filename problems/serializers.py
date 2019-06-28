from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class TagSerializer(serializers.ModelSerializer):
    problems = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('title', 'problems')


class ProblemDetailSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    solvers = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    class Meta:
        model = Problem
        fields = ('id', 'created_at', 'title', 'statement', 'no_of_solvers', 'tag', 'author', 'solvers', 'solved')


class ProblemsListSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    solvers = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)
    statement = serializers.CharField(write_only=True)
    no_of_solvers = serializers.IntegerField(read_only=True)

    class Meta:
        model = Problem
        fields = ('id', 'title', 'no_of_solvers', 'tag', 'solved', 'solvers', 'author', 'statement')


class UserProblemSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Problem
        fields = ('tag', 'title', 'id')


class UserSerializer(serializers.ModelSerializer):
    contributions = UserProblemSerializer(many=True, read_only=True)
    solves = UserProblemSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'contributions', 'solves', 'first_name', 'last_name', 'email')
