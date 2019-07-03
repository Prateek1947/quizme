import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth import hashers
from django.shortcuts import get_object_or_404


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
    tags = models.ManyToManyField(Tag, related_name='problems')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                               related_name='contributions')
    solvers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='solves', blank=True)
    solved = models.BooleanField(default=False)
    answer = models.CharField(max_length=128, blank=True, )

    def __str__(self):
        return self.title

    def set_answer(self, raw_answer):
        self.answer = hashers.make_password(raw_answer, salt='hello')

    def save(self, **kwargs):
        if self.pk is None:
            self.set_answer(self.answer)
        else:
            problem = get_object_or_404(Problem, pk=self.pk)
            if problem.answer != self.answer:
                self.set_answer(self.answer)
        super().save(**kwargs)
