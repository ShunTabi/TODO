from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL

# 定義
sql_1 = "SELECT GENRE_ID,GENRE_NAME,GENRE_DATE FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_2 = "SELECT GENRE_ID,GENRE_NAME,GENRE_DATE FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ? AND GENRE_ID = ?"
sql_3 = "INSERT INTO T_GENRE(GENRE_NAME,GENRE_DATE) VALUES(?,?)"
sql_4 = "UPDATE T_GENRE SET GENRE_NAME = ?,GENRE_DATE = ? WHERE GENRE_ID = ?"

def GENRE_TOP(req):
    if(req.method == 'GET'):
        sql_params = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_1, sql_params),
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


def GENRE_FORM_UPDATE(req,GENRE_ID):
    if(req.method == "GET"):
        sql_params = (
            0,GENRE_ID,
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
