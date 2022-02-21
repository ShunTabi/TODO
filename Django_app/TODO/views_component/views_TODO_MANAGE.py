from django.shortcuts import render
from django.http import JsonResponse
from . import views_setting_SQL,views_setting_SQLSTATEMENT,views_conf


def TODO_MANAGE_TOP(req,page,key1,key2,key_TODO):
    if(req.method == "GET"):
        if(key_TODO == views_conf.null_par):
            key_TODO = ""
        sql_params = (
            f"{key1}",
            f"{key2}",
            f"{key1}",
            f"{key2}",
            f"%{key_TODO}%",
            f"%{key_TODO}%",
            views_conf.sql_limit,
            views_conf.sql_limit*(page - 1),
        )
        sql_count_params = (
            f"{key1}",
            f"{key2}",
            f"{key1}",
            f"{key2}",
            f"%{key_TODO}%",
            f"%{key_TODO}%",
        )
        params = {
            "values":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_71_1,sql_params),
            "count":views_setting_SQL.SQL_SELECT(views_setting_SQLSTATEMENT.sql_71_2,sql_count_params),
            "sql_limit":views_conf.sql_limit,
            "values_nowtime":views_conf.nowtime,
            "values_nowtime7":views_conf.nowtime7,
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        return JsonResponse({"a":"a"})