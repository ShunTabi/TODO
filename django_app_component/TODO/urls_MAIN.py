from django.urls import path
from .views import views_MAIN


index = path(
    '',
    views_MAIN.index,
    name="index"
)