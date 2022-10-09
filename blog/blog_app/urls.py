from unicodedata import name
from . import views
from django.urls import path
urlpatterns = [
    path('articles/',views.list,name='articles'),
    path('category/<int:idCategory>',views.category,name='category'),
    path('article/<int:idArticle>',views.article,name='article'),
    path('create_article/',views.createArticle,name='createArticle'),
]