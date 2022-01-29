from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf

def GENRE_TOP(req,page):
    if(req.method == "GET"):
        sql_params = (
            views_conf.visible,
            views_conf.sql_limit,
            views_conf.sql_limit*(page - 1),
        )
        sql_count_params = (
            views_conf.visible,
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_11_1,sql_params),
            "count":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_11_2,sql_count_params),
            "sql_limit":views_conf.sql_limit,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"aaa":"aaa"})


def GENRE_FORM(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_NAME"],
        )
        views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_12,sql_params)
        return JsonResponse({"aaa":"aaa"})


def GENRE_UPDATE(req):
    if(req.method == "GET"):
        sql_params = (
            req.GET["GENRE_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_13,sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_NAME"],
            req.POST["GENRE_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_14,sql_params),
        }
        return JsonResponse(params)


def GENRE_DEL(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            views_conf.invisible,
            req.POST["GENRE_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_15,sql_params),
        }
        return JsonResponse(params)