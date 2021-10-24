from django.urls import path
from . import urls_GENRE, urls_MAIN, urls_TODO_HEADER, urls_TODO_DETAIL, urls_MEMO

urlpatterns = [
    # メイン
    urls_MAIN.index,
    urls_MAIN.Django_works,
    # 種別
    urls_GENRE.GENRE_TOP,
    urls_GENRE.GENRE_FORM,
    urls_GENRE.GENRE_FORM_UPDATE,
    urls_GENRE.GENRE_TOP_DEL,
    urls_GENRE.GENRE_DEL,
    # メモ
    urls_MEMO.MEMO_TOP,
<<<<<<< HEAD
    urls_MEMO.MEMO_TOP,
    urls_MEMO.MEMO_TOP_DEL,
    urls_MEMO.MEMO_TOP_DEL,
=======
    urls_MEMO.MEMO_FORM,
    urls_MEMO.MEMO_FORM_UPDATE,
    urls_MEMO.MEMO_TOP_DEL,
    urls_MEMO.MEMO_DEL,
>>>>>>> DEV
    # 作業
    urls_TODO_HEADER.TODO_HEADER_TOP,
    urls_TODO_HEADER.TODO_HEADER_FORM,
    urls_TODO_HEADER.TODO_HEADER_FORM_UPDATE,
    urls_TODO_HEADER.TODO_HEADER_TOP_DEL,
    urls_TODO_HEADER.TODO_HEADER_DEL,
    # 課題
    urls_TODO_DETAIL.TODO_DETAIL_TOP,
    urls_TODO_DETAIL.TODO_DETAIL_FORM,
    urls_TODO_DETAIL.TODO_DETAIL_FORM_UPDATE,
    urls_TODO_DETAIL.TODO_DETAIL_TOP_DEL,
    urls_TODO_DETAIL.TODO_DETAIL_DEL,
]
