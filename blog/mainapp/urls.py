from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('registro/',views.register_app,name='register'),
    path('login/',views.login_app,name='login'),
    path('logout/',views.logout_app,name='logout'),
]
