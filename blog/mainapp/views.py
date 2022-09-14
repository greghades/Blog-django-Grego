from turtle import title
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import ResgisterForm
# Create your views here.

def index(request):

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def welcome(request):
    print(request.user)
    return render(request,'welcome.html')

def services(request):
    return render(request, 'services.html')

def register_app(request):

    register_form = ResgisterForm()
    if request.method == 'POST':
        register_form = ResgisterForm(request.POST)
        if register_form.is_valid():
            messages.success(request,'Te has registrado correctamente')
            register_form.save()
            return redirect('/welcome')


    context = {
        'title':'Registro',
        'register_form':register_form,
    }
    return render(request,'users/registro.html',context)

def login_app(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.warning(request,'No existe el usuario')
    context = {
        'title':'Login',
    
    }

    return render(request,'users/login.html',context)

def logout_app(request):
     
    logout(request)

    return redirect('login')
