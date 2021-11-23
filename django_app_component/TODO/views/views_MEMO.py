from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_1 = "SELECT MEMO_ID,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_MEMO WHERE MEMO_VISIBLESTATUS = ?"
sql_2 = "SELECT MEMO_ID,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE TODO_DETAIL_ID = ? AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_2_count = "SELECT COUNT(*) FROM V_MEMO WHERE TODO_DETAIL_ID = ? AND MEMO_VISIBLESTATUS = ?"
sql_7 = "SELECT MEMO_ID,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE MEMO_NOTE LIKE ? AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_7_count = "SELECT COUNT(*) FROM V_MEMO WHERE MEMO_NOTE LIKE ? AND MEMO_VISIBLESTATUS = ?"
sql_3 = "INSERT INTO T_MEMO(TODO_DETAIL_ID,MEMO_NOTE,MEMO_DATE,MEMO_VISIBLESTATUS) VALUES(?,?,?,?)"
sql_4 = "SELECT MEMO_ID,TODO_DETAIL_ID,MEMO_NOTE,MEMO_DATE,MEMO_VISIBLESTATUS FROM V_MEMO WHERE MEMO_ID = ?"
sql_5 = "UPDATE T_MEMO SET TODO_DETAIL_ID = ?,MEMO_NOTE = ?,MEMO_DATE = ?,MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
sql_6 = "UPDATE T_MEMO SET MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
sql_limit = views_conf.sql_limit-3


def MEMO_TOP(req, MEMO_PAGE):
    TODO_DETAIL_ID = req.GET["TODO_DETAIL_ID"]
    value_MEMO_NOTE = req.GET["value_MEMO_NOTE"]
    if(TODO_DETAIL_ID == "0" and value_MEMO_NOTE == ""):
        sql_params = (
            0, sql_limit, sql_limit*(MEMO_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_DETAIL_ID != "0" and value_MEMO_NOTE == ""):
        sql_params = (
            TODO_DETAIL_ID, 0, sql_limit, sql_limit*(MEMO_PAGE-1),
        )
        sql_params_count = (
            TODO_DETAIL_ID, 0,
        )
        sql = sql_2
        sql_count = sql_2_count
    elif(TODO_DETAIL_ID == "0" and value_MEMO_NOTE != ""):
        value_MEMO_NOTE = f"%{value_MEMO_NOTE}%"
        sql_params = (
            value_MEMO_NOTE, 0, sql_limit, sql_limit*(MEMO_PAGE-1),
        )
        sql_params_count = (
            value_MEMO_NOTE, 0,
        )
        sql = sql_7
        sql_count = sql_7_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_DETAIL": views_COM.values_TODO_DETAIL(),
    }
    return JsonResponse(params)


def MEMO_TOP_DEL(req, MEMO_PAGE):
    sql_params = (
        1, sql_limit, sql_limit*(MEMO_PAGE-1),
    )
    sql_params_count = (
        1,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        "values_TODO_DETAIL": views_COM.values_TODO_DETAIL(),
    }
    return JsonResponse(params)


def MEMO_FORM(req):
    if(req.method == "GET"):
        params = {
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_3, sql_params)
        }
        return JsonResponse(params)


def MEMO_FORM_UPDATE(req, MEMO_ID):
    if(req.method == "GET"):
        sql_params = (
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_4, sql_params),
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_5, sql_params),
        }
        return JsonResponse(params)


def MEMO_DEL(req, MEMO_ID):
    if(req.method == 'POST'):
        sql_params = (
            1, MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_6, sql_params),
        }
        return JsonResponse(params)
