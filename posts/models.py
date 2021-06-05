from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from accounts.models import User
from django.urls.base import reverse
# Create your models here.


class Post(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.ForeignKey(User, related_name='user_posts',
                             on_delete=models.CASCADE)
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    workout = models.TextField()
    hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": {
                "username": self.name.username,
                'id': self.name.id
            }
        }

    def get_absolute_url(self):
        return reverse("post_show", kwargs={"pk": self.pk, "post.id": self.id, "name.id": self.name.id})

    def get_workout(self):
        return self.workout.split('\r\n')


class Like(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    liked = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, related_name="users_likes", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="users_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            'id': self.id,
            'user': {
                'username': self.user.username,
                'id': self.user.id,
                'post': {
                    'id': self.post.id,
                    'image': self.post.image,
                    'workout': self.post.workout,
                    'name': self.post.name.id

                }
            }
        }

    def get_absolute_url(self):
        return reverse("post_like", kwargs={"pk": self.pk, "post.id": self.post.id, "user.id": self.user.id})


class Comment(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.ForeignKey(
        User, related_name='user_comments', on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)

    def serialize(self):
        return {
            'id': self.id,
            'user': {
                'username': self.name.username
            },
            'comment': self.comment,
            'post': {
                'image': self.post.image,
                'workout': self.post.workout
            }
        }

    def get_absolute_url(self):
        return reverse("comment_create", kwargs={"pk": self.pk, "post.id": self.post.id, "name.id": self.name.id})
