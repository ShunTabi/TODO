from django.urls import path
from .views import views_MEMO


MEMO_TOP = path(
    'MEMO_TOP/<int:MEMO_PAGE>',
    views_MEMO.MEMO_TOP,
    name="MEMO_TOP"
)
MEMO_FORM = path(
    'MEMO_FORM/',
    views_MEMO.MEMO_FORM,
    name="MEMO_FORM"
)
MEMO_FORM_UPDATE = path(
    'MEMO_FORM/<int:MEMO_ID>',
    views_MEMO.MEMO_FORM_UPDATE,
    name="MEMO_FORM_UPDATE"
)
MEMO_TOP_DEL = path(
    'MEMO_TOP_DEL/<int:MEMO_PAGE>',
    views_MEMO.MEMO_TOP_DEL,
    name="MEMO_TOP_DEL"
)
MEMO_DEL = path(
    'MEMO_DEL/<int:MEMO_ID>',
    views_MEMO.MEMO_DEL,
    name="MEMO_DEL"
)
