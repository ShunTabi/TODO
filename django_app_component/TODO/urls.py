from django.urls import path
from . import urls_GENRE, urls_MAIN, urls_TODO, urls_TODO_HEADER, urls_TODO_DETAIL, urls_MEMO

urlpatterns = [
    urls_MAIN.index,
    urls_GENRE.GENRE_TOP,
    urls_GENRE.GENRE_FORM,
    urls_GENRE.GENRE_FORM_UPDATE,
    urls_GENRE.GENRE_TOP_DEL,
    urls_MEMO.MEMO_TOP,
    urls_MEMO.MEMO_TOP,
    urls_MEMO.MEMO_TOP_DEL,
    urls_MEMO.MEMO_TOP_DEL,
    # 10/16追記
    urls_TODO_HEADER.TODO_HEADER_TOP,
    urls_TODO_HEADER.TODO_HEADER_FORM,
    urls_TODO_HEADER.TODO_HEADER_FORM_UPDATE,
    urls_TODO_HEADER.TODO_HEADER_TOP_DEL,
    urls_TODO_DETAIL.TODO_DETAIL_TOP,
    urls_TODO_DETAIL.TODO_DETAIL_FORM,
    urls_TODO_DETAIL.TODO_DETAIL_FORM_UPDATE,
    urls_TODO_DETAIL.TODO_DETAIL_TOP_DEL,
    # 以下いらない
    urls_TODO.TODO_TOP,
    urls_TODO.TODO_FORM,
    urls_TODO.TODO_FORM_UPDATE,
    urls_TODO.TODO_TOP_DEL,
]
