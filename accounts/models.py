from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from posts.models import Post
# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
