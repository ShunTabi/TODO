from django.urls import path
from ..views_component import views_TODO_MANAGE

TODO_MANAGE_TOP = path("TODO_MANAGE_TOP/<int:page>/<str:key1>/<str:key2>/<str:key_TODO>",views_TODO_MANAGE.TODO_MANAGE_TOP,name="TODO_MANAGE_TOP")
