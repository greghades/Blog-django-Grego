from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from turtle import title
from unicodedata import name
from venv import create
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(verbose_name='Imagen',default='null',upload_to='article')
    public = models.BooleanField()
    user = models.ForeignKey(User,editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,null=True,blank=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
