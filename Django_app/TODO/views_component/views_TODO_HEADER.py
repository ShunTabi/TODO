from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf

def TODO_HEADER_TOP(req,page,key):
    if(req.method == "GET"):
        if(key == views_conf.null_par):
            key = ""
            print(key)
        sql_params = (
            f"%{key}%",
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.sql_limit,
            views_conf.sql_limit*(page - 1),
        )
        sql_count_params = (
            f"%{key}%",
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_31_1,sql_params),
            "count":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_31_2,sql_count_params),
            "sql_limit":views_conf.sql_limit,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"a":"a"})


def TODO_HEADER_FORM(req):
    if(req.method == "GET"):
        sql_params_GENRE = (
            views_conf.visible,
        )
        sql_params_PRIOR = (
            views_conf.visible,
        )
        params = {
            "values_GOAL":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_29,sql_params_GENRE),
            "values_PRIOR":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_61,sql_params_PRIOR),
            "values_nowtime":views_conf.nowtime,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GOAL_ID"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_HEADER_NAME"],
            req.POST["TODO_HEADER_ENDDATE"],
        )
        views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_32,sql_params)
        return JsonResponse({"a":"a"})


def TODO_HEADER_UPDATE(req):
    if(req.method == "GET"):
        sql_params = (
            req.GET["TODO_HEADER_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_33,sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["GOAL_ID"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_HEADER_NAME"],
            req.POST["TODO_HEADER_ENDDATE"],
            req.POST["TODO_HEADER_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_34,sql_params),
        }
        return JsonResponse(params)


def TODO_HEADER_DEL(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            views_conf.invisible,
            req.POST["TODO_HEADER_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_35,sql_params),
        }
        return JsonResponse(params)