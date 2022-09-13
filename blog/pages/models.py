from turtle import update
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    order = models.IntegerField(default=0)
    slug = models.CharField(unique=True, max_length=150)
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
