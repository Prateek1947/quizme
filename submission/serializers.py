from rest_framework import serializers
from submission.models import Submission
from user.models import User
from problems.models import Problem


class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False)
    problem = serializers.SlugRelatedField(slug_field='title', queryset=Problem.objects.all())
    solution_submitted = serializers.CharField(max_length=50, write_only=True)
    is_correct = serializers.BooleanField(read_only=True)

    class Meta:
        model = Submission
        fields = ('user', 'submitted_at', 'is_correct', 'problem', 'solution_submitted')
