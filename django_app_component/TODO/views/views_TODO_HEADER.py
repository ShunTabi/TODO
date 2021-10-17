from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf

# 定義
sql_1 = "SELECT TODO_HEADER_ID, TODO_HEADER_NAME , GENRE_NAME, TODO_HEADER_DATE FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? ORDER BY TODO_HEADER_DATE LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? ORDER BY TODO_HEADER_DATE"
sql_2 = "SELECT TODO_HEADER_ID, TODO_HEADER_NAME , GENRE_NAME, TODO_HEADER_DATE FROM V_TODO_HEADER WHERE TODO_HEADER_ID NOT IN (SELECT TODO_HEADER_ID FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?) ORDER BY TODO_HEADER_DATE LIMIT ? OFFSET ?"
sql_2_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_ID NOT IN (SELECT TODO_HEADER_ID FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?)"
sql_3 = "SELECT TODO_HEADER_ID,TODO_HEADER_NAME,GENRE_NAME,TODO_HEADER_DATE FROM V_TODO_HEADER WHERE TODO_HEADER_ID = ?"
sql_4 = "SELECT GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_5 = "SELECT PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ?"
sql_6 = "INSERT INTO T_TODO_HEADER(TODO_HEADER_NAME,GENRE_ID,TODO_HEADER_DATE) VALUES(?,(SELECT GENRE_ID FROM T_GENRE WHERE GENRE_NAME = ?),?)"
sql_7 = "UPDATE T_TODO_HEADER SET TODO_HEADER_NAME = ?,GENRE_ID = (SELECT GENRE_ID FROM T_GENRE WHERE GENRE_NAME = ?),TODO_HEADER_DATE = ? WHERE TODO_HEADER_ID = ?"
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
        sql_params_GENRE = (
            0,
        )
        sql_params_PRIOR = (
            0,
        )
        params = {
            "values_GENRE": views_SQL.SQL_SELECT(sql_4, sql_params_GENRE),
            "values_PRIOR": views_SQL.SQL_SELECT(sql_5, sql_params_PRIOR),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["GENRE_NAME"],
            req.POST["TODO_HEADER_DATE"],
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
        sql_params_GENRE = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_3, sql_params),
            "values_GENRE": views_SQL.SQL_SELECT(sql_4, sql_params_GENRE),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["GENRE_NAME"],
            req.POST["TODO_HEADER_DATE"],
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
