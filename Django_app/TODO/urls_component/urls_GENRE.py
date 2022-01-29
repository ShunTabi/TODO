from django.urls import path
from ..views_component import views_GENRE

GENRE_TOP = path("GENRE_TOP/<int:page>",views_GENRE.GENRE_TOP,name="GENRE_TOP")
GENRE_FORM = path("GENRE_FORM/",views_GENRE.GENRE_FORM,name="GENRE_FORM")
GENRE_UPDATE = path("GENRE_UPDATE/",views_GENRE.GENRE_UPDATE,name="GENRE_UPDATE")
GENRE_DEL = path("GENRE_DEL/",views_GENRE.GENRE_DEL,name="GENRE_DEL")
