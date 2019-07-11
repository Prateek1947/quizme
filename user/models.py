from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


# Create your models here.
def rename_file(instance, filename):
    extension = filename.split('.')[-1]
    file = str(uuid.uuid4()) + '.' + extension
    return os.path.join('users', file)


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)
    profile_picture = models.ImageField(blank=True, upload_to=rename_file)
