from django.urls import path
from .views import views_MAIN,views_GENRE,views_TODO,views_MEMO

urlpatterns = [
    path('',views_MAIN.index,name="index"),
    path('GENRE_TOP/',views_GENRE.GENRE_TOP,name="GENRE_TOP"),
    path('GENRE_FORM/',views_GENRE.GENRE_FORM,name="GENRE_FORM"),
    path('GENRE_FORM/<int:GENRE_ID>',views_GENRE.GENRE_FORM_UPDATE,name="GENRE_FORM_UPDATE"),
    path('GENRE_TOP_DEL/',views_GENRE.GENRE_TOP_DEL,name="GENRE_TOP_DEL"),
    path('TODO_TOP/',views_TODO.TODO_TOP,name="TODO_TOP"),
    path('TODO_FORM/',views_TODO.TODO_FORM,name="TODO_FORM_"),
    path('TODO_FORM/<int:TODO_ID>',views_TODO.TODO_FORM_UPDATE,name="TODO_FORM_UPDATE"),
    path('TODO_TOP_DEL/',views_TODO.TODO_TOP_DEL,name="TODO_TOP_DEL"),
    path('MEMO_TOP/',views_MEMO.MEMO_TOP,name="MEMO_TOP"),
    path('MEMO_FORM/',views_MEMO.MEMO_FORM,name="MEMO_FORM"),
    path('MEMO_FORM/<int:MEMO_ID>',views_MEMO.MEMO_FORM_UPDATE,name="MEMO_FORM_UPDATE"),
]
