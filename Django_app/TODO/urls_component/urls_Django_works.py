from django.contrib import admin
from django.urls import path,include
from ..views_component import views_Django_works

Django_works = path("Django_works/",views_Django_works.Django_works,name="Django_works")
index = path("",views_Django_works.index,name="index")
