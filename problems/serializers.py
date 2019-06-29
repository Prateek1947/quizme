from rest_framework import serializers
from problems.models import *


class TagSerializer(serializers.ModelSerializer):
    problems = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('title', 'problems')


class ProblemDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    solvers = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    class Meta:
        model = Problem
        fields = ('id', 'created_at', 'title', 'statement', 'no_of_solvers', 'tags', 'author', 'solvers', 'solved')


class ProblemsListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    solvers = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)
    statement = serializers.CharField(write_only=True)
    no_of_solvers = serializers.IntegerField(read_only=True)

    class Meta:
        model = Problem
        fields = ('id', 'title', 'no_of_solvers', 'tags', 'solved', 'solvers', 'author', 'statement')
