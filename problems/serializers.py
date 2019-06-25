from rest_framework import serializers
from .models import *


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('__all__')
