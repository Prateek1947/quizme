import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Problem(models.Model):
    created_at = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=20, unique=True)
    statement = models.TextField()
    no_of_solvers = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, related_name='problems')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='contributions')
    solvers = models.ManyToManyField(User, related_name='solves')
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
