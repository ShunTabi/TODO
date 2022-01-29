from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf

def MEMO_TOP(req,page,key):
    if(req.method == "GET"):
        if(key == views_conf.null_par):
            key = ""
        sql_params = (
            f"%{key}%",
            f"%{key}%",
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.sql_limit,
            views_conf.sql_limit*(page - 1),
        )
        sql_count_params = (
            f"%{key}%",
            f"%{key}%",
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
            views_conf.visible,
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_51_1,sql_params),
            "count":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_51_2,sql_count_params),
            "sql_limit":views_conf.sql_limit,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"a":"a"})


def MEMO_FORM(req):
    if(req.method == "GET"):
        if(req.GET["GOAL_ID"] == 'null'):
            sql_params_GOAL = (
                views_conf.visible,
            )
            sql_params_TODO_HEADER = (
                views_conf.visible,
            )
            sql_params_TODO_DETAIL = (
                views_conf.visible,
            )
            params = {
                "values_GOAL":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_29,sql_params_GOAL),
                "values_TODO_HEADER":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_39_1,sql_params_TODO_HEADER),
                "values_TODO_DETAIL":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_49_1,sql_params_TODO_DETAIL),
                "values_nowtime":views_conf.nowtime,
            }
            return JsonResponse(params)
        elif(req.GET["GOAL_ID"] != 'null'):
            sql_params_TODO_HEADER = (
                views_conf.visible,
                req.GET["GOAL_ID"],
            )
            sql_params_TODO_DETAIL = (
                views_conf.visible,
                req.GET["GOAL_ID"],
            )
            params = {
                "values_TODO_HEADER":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_39_2,sql_params_TODO_HEADER),
                "values_TODO_DETAIL":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_49_2,sql_params_TODO_DETAIL),
            }
            return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_CONTENT"],
        )
        views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_52,sql_params)
        return JsonResponse({"a":"a"})


def MEMO_UPDATE(req):
    if(req.method == "GET"):
        sql_params = (
            req.GET["MEMO_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_53,sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_CONTENT"],
            req.POST["MEMO_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_54,sql_params),
        }
        return JsonResponse(params)


def MEMO_DEL(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            views_conf.invisible,
            req.POST["MEMO_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_55,sql_params),
        }
        return JsonResponse(params)