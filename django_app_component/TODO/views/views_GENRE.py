from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf

# 定義
sql_1 = "SELECT GENRE_ID,GENRE_NAME,GENRE_DATE FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ? LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_2 = "SELECT GENRE_ID,GENRE_NAME,GENRE_DATE FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ? AND GENRE_ID = ?"
sql_3 = "INSERT INTO T_GENRE(GENRE_NAME,GENRE_DATE) VALUES(?,?)"
sql_4 = "UPDATE T_GENRE SET GENRE_NAME = ?,GENRE_DATE = ? WHERE GENRE_ID = ?"
sql_limit = views_conf.sql_limit


def GENRE_TOP(req, GENRE_PAGE):
    if(req.method == 'GET'):
        sql_params = (
            0, sql_limit, sql_limit*(GENRE_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        }
        return JsonResponse(params)


def GENRE_TOP_DEL(req, GENRE_PAGE):
    if(req.method == 'GET'):
        sql_params = (
            1, sql_limit, sql_limit*(GENRE_PAGE-1),
        )
        sql_params_count = (
            1,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        }
        return JsonResponse(params)


def GENRE_FORM(req):
    if(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_NAME"],
            req.POST["GENRE_DATE"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_3, sql_params),
        }
        return JsonResponse(params)


def GENRE_FORM_UPDATE(req, GENRE_ID):
    if(req.method == "GET"):
        sql_params = (
            0, GENRE_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_2, sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_NAME"],
            req.POST["GENRE_DATE"],
            req.POST["GENRE_ID"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_4, sql_params),
        }
        return JsonResponse(params)
