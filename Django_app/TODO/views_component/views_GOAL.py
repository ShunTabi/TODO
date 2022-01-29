from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf

def GOAL_TOP(req,page):
    if(req.method == "GET"):
        sql_params = (
            views_conf.visible,
            views_conf.visible,
            views_conf.sql_limit,
            views_conf.sql_limit*(page - 1),
        )
        sql_count_params = (
            views_conf.visible,
            views_conf.visible,
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_21_1,sql_params),
            "count":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_21_2,sql_count_params),
            "sql_limit":views_conf.sql_limit,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"a":"a"})


def GOAL_FORM(req):
    if(req.method == "GET"):
        sql_params_GENRE = (
            views_conf.visible,
        )
        params = {
            "values_GENRE":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_19,sql_params_GENRE),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_ID"],
            req.POST["GOAL_NAME"],
        )
        views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_22,sql_params)
        return JsonResponse({"a":"a"})


def GOAL_UPDATE(req):
    if(req.method == "GET"):
        sql_params = (
            req.GET["GOAL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_23,sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GENRE_ID"],
            req.POST["GOAL_NAME"],
            req.POST["GOAL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_24,sql_params),
        }
        return JsonResponse(params)


def GOAL_DEL(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            views_conf.invisible,
            req.POST["GOAL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_25,sql_params),
        }
        return JsonResponse(params)