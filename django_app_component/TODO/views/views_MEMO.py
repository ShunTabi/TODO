from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL

# 定義
sql_1 = "SELECT MEMO_ID,TODO_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ? LIMIT ?"
sql_2 = "SELECT TODO_NAME FROM V_TODO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ?"
sql_3 = "INSERT INTO T_MEMO(TODO_ID,MEMO_NOTE,MEMO_DATE) VALUES((SELECT TODO_ID FROM T_TODO WHERE TODO_NAME = ?),?,?)"
sql_4 = "SELECT MEMO_ID,TODO_NAME,MEMO_NOTE,MEMO_DATE FROM V_MEMO WHERE MEMO_ID = ?"
sql_5 = "UPDATE T_MEMO SET TODO_ID = (SELECT TODO_ID FROM T_TODO WHERE TODO_NAME = ?),MEMO_NOTE = ?,MEMO_DATE = ? WHERE MEMO_ID = ?"
sql_limit = 9

def MEMO_TOP(req):
    sql_params = (
        0, 0, 0,sql_limit,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
    }
    return JsonResponse(params)


def MEMO_FORM(req):
    if(req.method == "GET"):
        sql_params_TODO = (
            0,0,0,
        )
        params = {
            "values_TODO":views_SQL.SQL_SELECT(sql_2,sql_params_TODO)
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
        )
        params = {
            "values":views_SQL.SQL_DCL(sql_3,sql_params)
        }
        return JsonResponse(params)


def MEMO_FORM_UPDATE(req,MEMO_ID):
    if(req.method == "GET"):
        sql_params_TODO = (
            0,0,0,
        )
        sql_params = (
            MEMO_ID,
        )
        params = {
            "values":views_SQL.SQL_SELECT(sql_4,sql_params),
            "values_TODO":views_SQL.SQL_SELECT(sql_2,sql_params_TODO),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_NAME"],
            req.POST["MEMO_NOTE"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_ID"],
        )
        params = {
            "values":views_SQL.SQL_DCL(sql_5,sql_params),
        }
        return JsonResponse(params)