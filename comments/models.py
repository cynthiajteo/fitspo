from django.db import models
import uuid
from posts.models import *
from accounts.models import *
# Create your models here.


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
