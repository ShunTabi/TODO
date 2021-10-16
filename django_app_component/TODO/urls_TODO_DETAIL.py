from django.urls import path
from .views import views_TODO_DETAIL


TODO_DETAIL_TOP = path(
    'TODO_DETAIL_TOP/<int:TODO_DETAIL_PAGE>',
    views_TODO_DETAIL.TODO_DETAIL_TOP,
    name="TODO_DETAIL_TOP"
)
TODO_DETAIL_FORM = path(
    'TODO_DETAIL_FORM/',
    views_TODO_DETAIL.TODO_DETAIL_FORM,
    name="TODO_DETAIL_FORM"
)
TODO_DETAIL_FORM_UPDATE = path(
    'TODO_DETAIL_FORM/<int:TODO_DETAIL_ID>',
    views_TODO_DETAIL.TODO_DETAIL_FORM_UPDATE,
    name="TODO_DETAIL_FORM_UPDATE"
)
TODO_DETAIL_TOP_DEL = path(
    'TODO_DETAIL_TOP_DEL/<int:TODO_DETAIL_PAGE>',
    views_TODO_DETAIL.TODO_DETAIL_TOP_DEL,
    name="TODO_DETAIL_TOP_DEL"
)