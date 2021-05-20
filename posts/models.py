from django.db import models
import uuid
from cloudinary.models import CloudinaryField
# from accounts.models import User
from django.conf import settings
# Create your models here.


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts',
                             on_delete=models.CASCADE, default=None)
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    workout = models.TextField()
    hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
