from django.urls import path
from ..views_component import views_MEMO

MEMO_TOP = path("MEMO_TOP/<int:page>/<str:key>",views_MEMO.MEMO_TOP,name="MEMO_TOP")
MEMO_FORM = path("MEMO_FORM/",views_MEMO.MEMO_FORM,name="MEMO_FORM")
MEMO_UPDATE = path("MEMO_UPDATE/",views_MEMO.MEMO_UPDATE,name="MEMO_UPDATE")
MEMO_DEL = path("MEMO_DEL/",views_MEMO.MEMO_DEL,name="MEMO_DEL")
