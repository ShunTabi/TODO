from django.urls import path
from ..views_component import views_TODO_HEADER

TODO_HEADER_TOP = path("TODO_HEADER_TOP/<int:page>/<str:key>",views_TODO_HEADER.TODO_HEADER_TOP,name="TODO_HEADER_TOP")
TODO_HEADER_FORM = path("TODO_HEADER_FORM/",views_TODO_HEADER.TODO_HEADER_FORM,name="TODO_HEADER_FORM")
TODO_HEADER_UPDATE = path("TODO_HEADER_UPDATE/",views_TODO_HEADER.TODO_HEADER_UPDATE,name="TODO_HEADER_UPDATE")
TODO_HEADER_DEL = path("TODO_HEADER_DEL/",views_TODO_HEADER.TODO_HEADER_DEL,name="TODO_HEADER_DEL")