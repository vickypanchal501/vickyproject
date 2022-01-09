from django.contrib import admin
from django.urls import path
from vickyapp import views

urlpatterns = [
   
    path('', views.index,name= 'vickyapp'),
    path('about', views.about,name= 'about')
]
