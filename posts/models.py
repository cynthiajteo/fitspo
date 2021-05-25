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

            }
        }

    def get_absolute_url(self):
        return reverse("post_show", kwargs={"pk": self.pk, "post.id": self.id, "name.id": self.name.id})


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
