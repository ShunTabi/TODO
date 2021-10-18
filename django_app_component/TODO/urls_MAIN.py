from django.urls import path
from .views import views_MAIN


index = path(
    '',
    views_MAIN.index,
    name="index"
)
Django_works = path(
    'Django_works/',
    views_MAIN.Django_works,
    name="Django_works"
)