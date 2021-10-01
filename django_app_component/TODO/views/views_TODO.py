from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL

#定義
sql_1 = "SELECT TODO_ID,TODO_NAME,GENRE_NAME,PRIOR_SUBNAME,TODO_STARTDATE,TODO_ENDDATE FROM V_TODO WHERE GENRE_VISIBLESTATUS = ? AND PRIOR_VISIBLESTATUS = ? AND TODO_VISIBLESTATUS = ? ORDER BY TODO_ENDDATE LIMIT ?"
sql_2 = "SELECT TODO_ID,TODO_NAME,GENRE_NAME,PRIOR_NAME,TODO_STARTDATE,TODO_ENDDATE FROM V_TODO WHERE TODO_ID = ?"
sql_3 = "SELECT GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_4 = "SELECT PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ?"
sql_5 = "INSERT INTO T_TODO(TODO_NAME,GENRE_ID,PRIOR_ID,TODO_STARTDATE,TODO_ENDDATE) VALUES(?,(SELECT GENRE_ID FROM T_GENRE WHERE GENRE_NAME = ?),(SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_NAME = ?),?,?)"
sql_6 = "UPDATE T_TODO SET TODO_NAME = ?,GENRE_ID = (SELECT GENRE_ID FROM T_GENRE WHERE GENRE_NAME = ?),PRIOR_ID = (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_NAME = ?),TODO_STARTDATE = ?,TODO_ENDDATE = ? WHERE TODO_ID = ?"
sql_limit = 9


def TODO_TOP(req):
    sql_params = (
        0, 0, 0,sql_limit,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
    }
    return JsonResponse(params)


def TODO_TOP_DEL(req):
    sql_params = (
        0, 0, 1,sql_limit,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
    }
    return JsonResponse(params)


def TODO_FORM(req):
    if(req.method == "GET"):
        sql_params_GENRE = (
            0,
        )
        sql_params_PRIOR = (
            0,
        )
        params = {
            "values_GENRE": views_SQL.SQL_SELECT(sql_3, sql_params_GENRE),
            "values_PRIOR": views_SQL.SQL_SELECT(sql_4, sql_params_PRIOR),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_NAME"],
            req.POST["GENRE_NAME"],
            req.POST["PRIOR_NAME"],
            req.POST["TODO_STARTDATE"],
            req.POST["TODO_ENDDATE"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_5, sql_params),
        }
        return JsonResponse(params)


def TODO_FORM_UPDATE(req,TODO_ID):
    if(req.method == "GET"):
        sql_params = (
            TODO_ID,
        )
        sql_params_GENRE = (
            0,
        )
        sql_params_PRIOR = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_2, sql_params),
            "values_GENRE": views_SQL.SQL_SELECT(sql_3, sql_params_GENRE),
            "values_PRIOR": views_SQL.SQL_SELECT(sql_4, sql_params_PRIOR),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_NAME"],
            req.POST["GENRE_NAME"],
            req.POST["PRIOR_NAME"],
            req.POST["TODO_STARTDATE"],
            req.POST["TODO_ENDDATE"],
            req.POST["TODO_ID"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_6, sql_params),
        }
        return JsonResponse(params)