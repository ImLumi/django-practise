import uuid
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(BaseModel):
    author = models.CharField(max_length=255)
    text = models.TextField()


class Topic(BaseModel):
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment)
