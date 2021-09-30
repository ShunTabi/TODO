from django.contrib import admin
from django.urls import path,include
from .views import views_TIME

urlpatterns = [
    path("NOW_TIME/",views_TIME.NOW_TIME,name="NOW_TIME")
]
