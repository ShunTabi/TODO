from django.urls import path
from ..views_component import views_TODO_DETAIL

TODO_DETAIL_TOP = path("TODO_DETAIL_TOP/<int:page>/<str:key_TODO>/<str:key_STATUS>",views_TODO_DETAIL.TODO_DETAIL_TOP,name="TODO_DETAIL_TOP")
TODO_DETAIL_FORM = path("TODO_DETAIL_FORM/",views_TODO_DETAIL.TODO_DETAIL_FORM,name="TODO_DETAIL_FORM")
TODO_DETAIL_UPDATE = path("TODO_DETAIL_UPDATE/",views_TODO_DETAIL.TODO_DETAIL_UPDATE,name="TODO_DETAIL_UPDATE")
TODO_DETAIL_DEL = path("TODO_DETAIL_DEL/",views_TODO_DETAIL.TODO_DETAIL_DEL,name="TODO_DETAIL_DEL")