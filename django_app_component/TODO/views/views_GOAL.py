from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf,views_COM

# 定義
sql_limit = views_conf.sql_limit


def GOAL_TOP(req, GOAL_PAGE):
    if(req.method == 'GET'):
        sql_1 = "SELECT GOAL_ID,GENRE_NAME,GOAL_NAME,GOAL_DATE FROM V_GOAL WHERE GOAL_VISIBLESTATUS=? ORDER BY GOAL_DATE DESC,GOAL_ID DESC LIMIT ? OFFSET ?"
        sql_1_count = "SELECT COUNT(*) FROM V_GOAL WHERE GOAL_VISIBLESTATUS=?"
        sql_params = (
            0, sql_limit, sql_limit*(GOAL_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        }
        return JsonResponse(params)


def GOAL_TOP_DEL(req, GOAL_PAGE):
    if(req.method == 'GET'):
        sql_1 = "SELECT GOAL_ID,GENRE_NAME,GOAL_NAME,GOAL_DATE FROM V_GOAL WHERE GOAL_VISIBLESTATUS=? ORDER BY GOAL_DATE DESC,GOAL_ID DESC LIMIT ? OFFSET ?"
        sql_1_count = "SELECT COUNT(*) FROM V_GOAL WHERE GOAL_VISIBLESTATUS=?"
        sql_params = (
            1, sql_limit, sql_limit*(GOAL_PAGE-1),
        )
        sql_params_count = (
            1,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
            "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
        }
        return JsonResponse(params)


def GOAL_FORM(req):
    if(req.method == "GET"):
        params = {
            "values_GENRE": views_COM.values_GENRE(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_3 = "INSERT INTO T_GOAL(GOAL_NAME,GENRE_ID,GOAL_DATE,GOAL_VISIBLESTATUS) VALUES(?,?,?,?)"
        sql_params = (
            req.POST["GOAL_NAME"],
            req.POST["GENRE_ID"],
            req.POST["GOAL_DATE"],
            req.POST["GOAL_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DML(sql_3, sql_params),
        }
        return JsonResponse(params)


def GOAL_FORM_UPDATE(req, GOAL_ID):
    if(req.method == "GET"):
        sql_4 = "SELECT GOAL_ID,GOAL_NAME,GENRE_ID,GOAL_DATE,GOAL_VISIBLESTATUS FROM T_GOAL WHERE GOAL_ID = ?"
        sql_params = (
            GOAL_ID,
        )
        params = {
            "values":views_SQL.SQL_SELECT(sql_4,sql_params),
            "values_GENRE": views_COM.values_GENRE(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_5 = "UPDATE T_GOAL SET GOAL_NAME = ?,GENRE_ID = ?,GOAL_DATE = ?,GOAl_VISIBLESTATUS = ? WHERE GOAL_ID = ?"
        sql_params = (
            req.POST["GOAL_NAME"],
            req.POST["GENRE_ID"],
            req.POST["GOAL_DATE"],
            req.POST["GOAL_VISIBLESTATUS"],
            GOAL_ID
        )
        params = {
            "values": views_SQL.SQL_DML(sql_5, sql_params),
        }
        return JsonResponse(params)


def GOAL_DEL(req, GOAL_ID):
    if(req.method == 'POST'):
        sql_6 = "UPDATE T_GOAL SET GOAL_VISIBLESTATUS = ? WHERE GOAL_ID = ?"
        sql_params = (
             1, GOAL_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_6, sql_params),
        }
        return JsonResponse(params)