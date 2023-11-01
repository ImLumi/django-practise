import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Topic(BaseModel):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="+",
    )

class Comment(BaseModel):
    author = models.CharField(max_length=255)
    text = models.TextField()
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)

