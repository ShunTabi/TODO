from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf,views_COM

# 定義

sql_1 = "SELECT TODO_HEADER_ID,GENRE_NAME,TODO_HEADER_NAME,TODO_HEADER_DATE,TODO_HEADER_VISIBLESTATUS FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? ORDER BY TODO_HEADER_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? ORDER BY TODO_HEADER_DATE"
sql_2 = "SELECT TODO_HEADER_ID,GENRE_NAME,TODO_HEADER_NAME, TODO_HEADER_DATE,TODO_HEADER_VISIBLESTATUS FROM V_TODO_HEADER WHERE TODO_HEADER_ID NOT IN (SELECT TODO_HEADER_ID FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?) ORDER BY TODO_HEADER_DATE LIMIT ? OFFSET ?"
sql_2_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_ID NOT IN (SELECT TODO_HEADER_ID FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?)"
sql_3 = "SELECT TODO_HEADER_ID,TODO_HEADER_NAME,GENRE_ID,TODO_HEADER_DATE,TODO_HEADER_VISIBLESTATUS FROM V_TODO_HEADER WHERE TODO_HEADER_ID = ?"
sql_6 = "INSERT INTO T_TODO_HEADER(TODO_HEADER_NAME,GENRE_ID,TODO_HEADER_DATE,TODO_HEADER_VISIBLESTATUS) VALUES(?,?,?,?)"
sql_7 = "UPDATE T_TODO_HEADER SET TODO_HEADER_NAME = ?,GENRE_ID = ?,TODO_HEADER_DATE = ?,TODO_HEADER_VISIBLESTATUS = ? WHERE TODO_HEADER_ID = ?"
sql_8 = "UPDATE T_TODO_HEADER SET TODO_HEADER_VISIBLESTATUS = ? WHERE TODO_HEADER_ID = ?"
sql_limit = views_conf.sql_limit


def TODO_HEADER_TOP(req, TODO_PAGE):
    if(req.method == "GET"):
        sql_params = (
            0, sql_limit, sql_limit*(TODO_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        }
        return JsonResponse(params)


def TODO_HEADER_TOP_DEL(req, TODO_PAGE):
    if(req.method == "GET"):
        sql_params = (
            0, sql_limit, sql_limit*(TODO_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_2, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_2_count, sql_params_count),
        }
    return JsonResponse(params)


def TODO_HEADER_FORM(req):
    if(req.method == "GET"):
        params = {
            "values_GENRE": views_COM.values_GENRE(),
            "values_PRIOR": views_COM.values_PRIOR(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["GENRE_ID"],
            req.POST["TODO_HEADER_DATE"],
            req.POST["TODO_HEADER_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_6, sql_params),
        }
        return JsonResponse(params)


def TODO_HEADER_FORM_UPDATE(req, TODO_HEADER_ID):
    if(req.method == "GET"):
        sql_params = (
            TODO_HEADER_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_3, sql_params),
            "values_GENRE": views_COM.values_GENRE(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["GENRE_ID"],
            req.POST["TODO_HEADER_DATE"],
            req.POST["TODO_HEADER_VISIBLESTATUS"],
            TODO_HEADER_ID
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_7, sql_params),
        }
        return JsonResponse(params)


def TODO_HEADER_DEL(req, TODO_HEADER_ID):
    if(req.method == 'POST'):
        sql_params = (
            1, TODO_HEADER_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_8, sql_params),
        }
        return JsonResponse(params)
