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
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=False)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE, related_name='comments')

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
