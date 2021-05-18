from django.db import models
import uuid

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    # image = CloudinaryField('image')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    workout = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
