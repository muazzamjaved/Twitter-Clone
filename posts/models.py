from email.mime import image
from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField(
        'image', db_index=True, blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likecount = models.IntegerField(
        'like_count', blank=True, default=0
    )


# Create your models here.
