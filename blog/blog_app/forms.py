from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Article
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
