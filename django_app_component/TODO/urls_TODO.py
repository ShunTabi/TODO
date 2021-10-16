from django.urls import path
from .views import views_TODO


TODO_TOP = path(
    'TODO_TOP/<int:TODO_PAGE>',
    views_TODO.TODO_TOP,
    name="TODO_TOP"
)
TODO_FORM = path(
    'TODO_FORM/',
    views_TODO.TODO_FORM,
    name="TODO_FORM_"
)
TODO_FORM_UPDATE = path(
    'TODO_FORM/<int:TODO_ID>',
    views_TODO.TODO_FORM_UPDATE,
    name="TODO_FORM_UPDATE"
)
TODO_TOP_DEL = path(
    'TODO_TOP_DEL/<int:TODO_PAGE>',
    views_TODO.TODO_TOP_DEL,
    name="TODO_TOP_DEL"
)