from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf

# 定義
<<<<<<< HEAD
sql_1 = "SELECT MEMO_ID,TODO_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ? AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_MEMO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ? AND MEMO_VISIBLESTATUS = ?"
sql_2 = "SELECT TODO_NAME FROM V_TODO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ?"
sql_3 = "INSERT INTO T_MEMO(TODO_ID,MEMO_NOTE,MEMO_DATE) VALUES((SELECT TODO_ID FROM T_TODO WHERE TODO_NAME = ?),?,?)"
sql_4 = "SELECT MEMO_ID,TODO_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE MEMO_ID = ?"
sql_5 = "UPDATE T_MEMO SET TODO_ID = (SELECT TODO_ID FROM T_TODO WHERE TODO_NAME = ?),MEMO_NOTE = ?,MEMO_DATE = ? WHERE MEMO_ID = ?"
=======
sql_1 = "SELECT MEMO_ID,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_MEMO WHERE MEMO_VISIBLESTATUS = ?"
sql_2 = "SELECT TODO_DETAIL_NAME FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ?"
sql_3 = "INSERT INTO T_MEMO(TODO_DETAIL_ID,MEMO_NOTE,MEMO_DATE,MEMO_VISIBLESTATUS) VALUES((SELECT TODO_DETAIL_ID FROM T_TODO_DETAIL WHERE TODO_DETAIL_NAME = ?),?,?,?)"
sql_4 = "SELECT MEMO_ID,TODO_DETAIL_NAME,MEMO_NOTE,MEMO_DATE,MEMO_VISIBLESTATUS FROM V_MEMO WHERE MEMO_ID = ?"
sql_5 = "UPDATE T_MEMO SET TODO_DETAIL_ID = (SELECT TODO_DETAIL_ID FROM T_TODO_DETAIL WHERE TODO_DETAIL_NAME = ?),MEMO_NOTE = ?,MEMO_DATE = ?,MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
sql_6 = "UPDATE T_MEMO SET MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
>>>>>>> DEV
sql_limit = views_conf.sql_limit


def MEMO_TOP(req, MEMO_PAGE):
    sql_params = (
<<<<<<< HEAD
        0, 0, 0, 0, sql_limit, sql_limit*(MEMO_PAGE-1),
    )
    sql_params_count = (
        0, 0, 0, 0,
=======
        0, sql_limit, sql_limit*(MEMO_PAGE-1),
    )
    sql_params_count = (
        0,
>>>>>>> DEV
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
    }
    return JsonResponse(params)


def MEMO_TOP_DEL(req, MEMO_PAGE):
    sql_params = (
<<<<<<< HEAD
        0, 0, 0, 1, sql_limit, sql_limit*(MEMO_PAGE-1),
    )
    sql_params_count = (
        0, 0, 0, 1,
=======
        1, sql_limit, sql_limit*(MEMO_PAGE-1),
    )
    sql_params_count = (
        1,
>>>>>>> DEV
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
    }
    return JsonResponse(params)


def MEMO_FORM(req):
    if(req.method == "GET"):
<<<<<<< HEAD
        sql_params_TODO = (
            0, 0, 0,
        )
        params = {
            "values_TODO": views_SQL.SQL_SELECT(sql_2, sql_params_TODO)
=======
        sql_params_TODO_DETAIL = (
            0,
        )
        params = {
            "values_TODO_DETAIL": views_SQL.SQL_SELECT(sql_2, sql_params_TODO_DETAIL)
>>>>>>> DEV
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
<<<<<<< HEAD
            req.POST["TODO_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
=======
            req.POST["TODO_DETAIL_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
>>>>>>> DEV
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_3, sql_params)
        }
        return JsonResponse(params)


def MEMO_FORM_UPDATE(req, MEMO_ID):
    if(req.method == "GET"):
<<<<<<< HEAD
        sql_params_TODO = (
            0, 0, 0,
=======
        sql_params_TODO_DETAIL = (
            0,
>>>>>>> DEV
        )
        sql_params = (
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_4, sql_params),
<<<<<<< HEAD
            "values_TODO": views_SQL.SQL_SELECT(sql_2, sql_params_TODO),
=======
            "values_TODO_DETAIL": views_SQL.SQL_SELECT(sql_2, sql_params_TODO_DETAIL),
>>>>>>> DEV
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
<<<<<<< HEAD
            req.POST["TODO_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
=======
            req.POST["TODO_DETAIL_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
>>>>>>> DEV
            req.POST["MEMO_ID"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_5, sql_params),
        }
        return JsonResponse(params)
<<<<<<< HEAD
=======


def MEMO_DEL(req, MEMO_ID):
    if(req.method == 'POST'):
        sql_params = (
            1, MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_6, sql_params),
        }
        return JsonResponse(params)
>>>>>>> DEV