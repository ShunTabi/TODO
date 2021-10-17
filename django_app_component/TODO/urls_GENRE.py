from django.urls import path
from .views import views_GENRE


GENRE_TOP = path(
    'GENRE_TOP/<int:GENRE_PAGE>',
    views_GENRE.GENRE_TOP,
    name="GENRE_TOP"
)

GENRE_FORM = path(
    'GENRE_FORM/',
    views_GENRE.GENRE_FORM,
    name="GENRE_FORM"
)
GENRE_FORM_UPDATE = path(
    'GENRE_FORM/<int:GENRE_ID>',
    views_GENRE.GENRE_FORM_UPDATE,
    name="GENRE_FORM_UPDATE"
)
GENRE_TOP_DEL = path(
    'GENRE_TOP_DEL/<int:GENRE_PAGE>',
    views_GENRE.GENRE_TOP_DEL,
    name="GENRE_TOP_DEL"
)
GENRE_DEL = path(
    'GENRE_DEL/<int:GENRE_ID>',
    views_GENRE.GENRE_DEL,
    name="GENRE_DEL"
)
