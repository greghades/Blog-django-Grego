from contextlib import ContextDecorator
from email.mime import image
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Article,Category
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def list(request):
    articles = Article.objects.filter(public=True).all()
    context = {'articles':articles}
    return render(request,'articles/list.html',context)

@login_required(login_url='login')
def category(request,idCategory):
    category = Category.objects.get(id=idCategory)
    articles = Article.objects.filter(categories=idCategory).all()

    context = {
        'category':category,
        'articles':articles,
        }

    return render(request,'categories/category.html',context)

@login_required(login_url='login')
def article(request,idArticle):
    article = Article.objects.get(id=idArticle)

    context = {
        'article':article,
    }
    return render(request,'articles/article.html',context)

@login_required(login_url='login')
def createArticle(request):
    articleForm = ArticleForm()
   
    if request.method == 'POST':
        
        articleForm = ArticleForm(request.POST, request.FILES)
        if articleForm.is_valid(): 
            obj = articleForm.save(commit=False)
            print(obj.image)
            obj.user_id = request.user.id
            obj.save()
        return redirect('articles')
    context = {
        'articleForm':articleForm,
    }
    return render(request,'articles/articleForm.html',context)