"""foodempire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user.views import index,menu,reservation1,contact,about,gallery,stuff,blog,blog_single
from user.views import createreservation,reservation1


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/',index,name='index'),
    path('menu/',menu,name='menu'),
    path('reservation/',reservation1,name='reservation'),
    path('rev/',createreservation.as_view(),name='createreservation'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('gallery/',gallery,name='gallery'),
    path('stuff/',stuff,name='stuff'),
    path('blog/',blog,name='blog'),
    path('blog-single/',blog_single,name='blog-single'),
]
