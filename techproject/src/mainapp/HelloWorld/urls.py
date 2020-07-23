from django.contrib import admin
from django.urls import path, include
#from the same directory, import the views file
from . import views

#this registers our index function from views.py to a URL
urlpatterns = [
    path('', views.helloWorld,
name='index')
]