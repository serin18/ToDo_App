"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from reminder.views import Registerview,signviw,Signout,taskview,Taskupdate,Taskdelete,Tableview,Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',Registerview.as_view(),name="reg"),
    path('login',signviw.as_view(),name="login"),
    path('logout/',Signout.as_view()),
    path('index/',taskview.as_view(),name="index"),
    path('logout/',Signout.as_view(),name="logout"),
    path("index/edit/<int:pk>",Taskupdate.as_view(),name="edit"),
    path('index/delete/<int:pk>',Taskdelete.as_view(),name="delete"),
    path('table/',Tableview.as_view(),name="table"),
    path('',Homeview.as_view(),name="home"),
    path('api/',include("api.urls"))
    


]
