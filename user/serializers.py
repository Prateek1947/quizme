from rest_framework import serializers
from problems.models import *
from user.models import User


class UserProblemSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Problem
        fields = ('tags', 'title', 'id')


class UserSerializer(serializers.ModelSerializer):
    contributions = UserProblemSerializer(many=True, read_only=True)
    solves = UserProblemSerializer(many=True, read_only=True)
    following = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', many=True)
    followers = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'contributions', 'solves', 'first_name', 'last_name', 'email', 'following', 'followers',
            'profile_picture')
