from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.CharField(max_length=20)
    statement = models.CharField(max_length=200)
    solvedBy = models.IntegerField()
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title