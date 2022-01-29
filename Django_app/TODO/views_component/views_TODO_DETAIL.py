from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf

def TODO_DETAIL_TOP(req,page,key_TODO,key_STATUS):
    if(req.method == "GET"):
        if(key_TODO == views_conf.null_par):
            key_TODO = ""
        if(key_STATUS == views_conf.null_par):
            sql_params = (
                f"%{key_TODO}%",
                f"%{key_TODO}%",
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.sql_limit,
                views_conf.sql_limit*(page - 1),
            )
            sql = views_setting_SQLSTATEMENT.sql_41_1_1
            sql_count_params = (
                f"%{key_TODO}%",
                f"%{key_TODO}%",
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
            )
            sql_count = views_setting_SQLSTATEMENT.sql_41_2_1
        else:
            sql_params = (
                f"%{key_TODO}%",
                f"%{key_TODO}%",
                key_STATUS,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.sql_limit,
                views_conf.sql_limit*(page - 1),
            )
            sql = views_setting_SQLSTATEMENT.sql_41_1_2
            sql_count_params = (
                f"%{key_TODO}%",
                f"%{key_TODO}%",
                key_STATUS,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
                views_conf.visible,
            )
            sql_count = views_setting_SQLSTATEMENT.sql_41_2_2
        sql_params_STATUS = (
                views_conf.visible,
            )
        params = {
            "values":views_setting_SQL.SQL_SELECT(sql,sql_params),
            "count":views_setting_SQL.SQL_SELECT(sql_count,sql_count_params),
            "sql_limit":views_conf.sql_limit,
            "values_STATUS":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_62,sql_params_STATUS),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"a":"a"})


def TODO_DETAIL_FORM(req):
    if(req.method == "GET"):
        if(req.GET["GOAL_ID"] == 'null'):
            sql_params_GOAL = (
                views_conf.visible,
            )
            sql_params_STATUS = (
                views_conf.visible,
            )
            sql_params_TODO_HEADER = (
                views_conf.visible,
            )
            params = {
                "values_GOAL":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_29,sql_params_GOAL),
                "values_STATUS":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_62,sql_params_STATUS),
                "values_TODO_HEADER":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_39_1,sql_params_TODO_HEADER),
                "values_nowtime":views_conf.nowtime,
            }
            return JsonResponse(params)
        else:
            sql_params_TODO_HEADER = (
                views_conf.visible,
                req.GET["GOAL_ID"],
            )
            params = {
                "values_TODO_HEADER":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_39_2,sql_params_TODO_HEADER),
            }
            return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["STATUS_ID"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
        )
        views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_42,sql_params)
        return JsonResponse({"a":"a"})


def TODO_DETAIL_UPDATE(req):
    if(req.method == "GET"):
        sql_params = (
            req.GET["TODO_DETAIL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_43,sql_params),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["STATUS_ID"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
            req.POST["TODO_DETAIL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_44,sql_params),
        }
        return JsonResponse(params)


def TODO_DETAIL_DEL(req):
    if(req.method == "GET"):
        return JsonResponse({"aaa":"aaa"})
    elif(req.method == "POST"):
        sql_params = (
            views_conf.invisible,
            req.POST["TODO_DETAIL_ID"],
        )
        params = {
            "values":views_setting_SQL.SQL_DML(views_setting_SQLSTATEMENT.sql_45,sql_params),
        }
        return JsonResponse(params)