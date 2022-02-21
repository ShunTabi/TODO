import imp
from django.contrib import admin
from django.urls import path,include
from .urls_component import urls_Django_works,urls_GENRE,urls_GOAL,urls_TODO_HEADER,urls_TODO_DETAIL,urls_MEMO,urls_TODO_MANAGE

urlpatterns = [
    #1.Django_works
    urls_Django_works.index,
    urls_Django_works.Django_works,
    #2.GENRE
    urls_GENRE.GENRE_TOP,
    urls_GENRE.GENRE_FORM,
    urls_GENRE.GENRE_UPDATE,
    urls_GENRE.GENRE_DEL,
    #3.GOAL
    urls_GOAL.GOAL_TOP,
    urls_GOAL.GOAL_FORM,
    urls_GOAL.GOAL_UPDATE,
    urls_GOAL.GOAL_DEL,
    #4.TODO_HEADER
    urls_TODO_HEADER.TODO_HEADER_TOP,
    urls_TODO_HEADER.TODO_HEADER_FORM,
    urls_TODO_HEADER.TODO_HEADER_UPDATE,
    urls_TODO_HEADER.TODO_HEADER_DEL,
    #5.TODO_DETAIL
    urls_TODO_DETAIL.TODO_DETAIL_TOP,
    urls_TODO_DETAIL.TODO_DETAIL_FORM,
    urls_TODO_DETAIL.TODO_DETAIL_UPDATE,
    urls_TODO_DETAIL.TODO_DETAIL_DEL,
    #6.MEMO
    urls_MEMO.MEMO_TOP,
    urls_MEMO.MEMO_FORM,
    urls_MEMO.MEMO_UPDATE,
    urls_MEMO.MEMO_DEL,
    #7.TODO_MANAGE
    urls_TODO_MANAGE.TODO_MANAGE_TOP,
]