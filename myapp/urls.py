from django.contrib import admin
from django.urls import include,path
from . import views
from django.contrib.auth import views as authentication_view 

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('profile', views.profilepage, name='profile'),
    path('login/', authentication_view.LoginView.as_view(template_name="myapp/login.html"), name="login"),
    path('logout/', authentication_view.LogoutView.as_view(template_name="myapp/logout.html"), name="logout")
]
