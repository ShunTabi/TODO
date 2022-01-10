from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_limit = views_conf.sql_limit


def TODO_HEADER_TOP(req, TODO_HEADER_PAGE):
    sql_1 = "SELECT TODO_HEADER_ID,GOAL_NAME,TODO_HEADER_NAME,PRIOR_SUBNAME,TODO_HEADER_STARTDATE,TODO_HEADER_ENDDATE FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? "
    sql_1_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? "
    sql_1_option = ""
    GOAL_ID = req.GET["GOAL_ID"]
    PRIOR_ID = req.GET["PRIOR_ID"]
    sql_params = [0]
    sql_count_params = [0]
    if(GOAL_ID != "0"):
        sql_1_option += "AND GOAL_ID = ? "
        sql_params.append(GOAL_ID)
        sql_count_params.append(GOAL_ID)
    if(PRIOR_ID != "0"):
        sql_1_option += "AND PRIOR_ID = ? "
        sql_params.append(PRIOR_ID)
        sql_count_params.append(PRIOR_ID)
    sql_params.append(sql_limit)
    sql_params.append(sql_limit*(TODO_HEADER_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY TODO_HEADER_ENDDATE,TODO_HEADER_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_GOAL": views_COM.values_GOAL(),
        "values_PRIOR": views_COM.values_PRIOR(),
    }
    return JsonResponse(params)


def TODO_HEADER_TOP_DEL(req, TODO_HEADER_PAGE):
    sql_1 = "SELECT TODO_HEADER_ID,GOAL_NAME,TODO_HEADER_NAME,PRIOR_SUBNAME,TODO_HEADER_STARTDATE,TODO_HEADER_ENDDATE FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? "
    sql_1_count = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? "
    sql_1_option = ""
    GOAL_ID = req.GET["GOAL_ID"]
    PRIOR_ID = req.GET["PRIOR_ID"]
    sql_1_params = [1]
    sql_1_count_params = [1]
    if(GOAL_ID != "0"):
        sql_1_option += "AND GOAL_ID = ? "
        sql_1_params.append(GOAL_ID)
        sql_1_count_params.append(GOAL_ID)
    if(PRIOR_ID != "0"):
        sql_1_option += "AND PRIOR_ID = ? "
        sql_1_params.append(PRIOR_ID)
        sql_1_count_params.append(PRIOR_ID)
    sql_1_params.append(sql_limit)
    sql_1_params.append(sql_limit*(TODO_HEADER_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY TODO_HEADER_ENDDATE,TODO_HEADER_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_1_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_1_count_params),
        "values_GOAL": views_COM.values_GOAL(),
        "values_PRIOR": views_COM.values_PRIOR(),
    }
    return JsonResponse(params)


def TODO_HEADER_FORM(req):
    sql_5 = "INSERT INTO T_TODO_HEADER(GOAL_ID,TODO_HEADER_NAME,PRIOR_ID,TODO_HEADER_STARTDATE,TODO_HEADER_ENDDATE,TODO_HEADER_VISIBLESTATUS) VALUES(?,?,?,?,?,?)"
    if(req.method == "GET"):
        params = {
            "values_PRIOR": views_COM.values_PRIOR(),
            "values_GOAL": views_COM.values_GOAL(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["GOAL_ID"],
            req.POST["TODO_HEADER_NAME"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_HEADER_STARTDATE"],
            req.POST["TODO_HEADER_ENDDATE"],
            req.POST["TODO_HEADER_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DML(sql_5, sql_params),
        }
        return JsonResponse(params)


def TODO_HEADER_FORM_UPDATE(req, TODO_HEADER_ID):
    if(req.method == "GET"):
        sql_6 = "SELECT TODO_HEADER_ID,GOAL_ID,TODO_HEADER_NAME,PRIOR_ID,TODO_HEADER_STARTDATE,TODO_HEADER_ENDDATE,TODO_HEADER_VISIBLESTATUS FROM T_TODO_HEADER WHERE TODO_HEADER_ID = ?"
        sql_params = (
            TODO_HEADER_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_6, sql_params),
            "values_PRIOR": views_COM.values_PRIOR(),
            "values_GOAL": views_COM.values_GOAL(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_7 = "UPDATE T_TODO_HEADER SET GOAL_ID = ?,TODO_HEADER_NAME = ?,PRIOR_ID = ?,TODO_HEADER_STARTDATE = ?,TODO_HEADER_ENDDATE = ?,TODO_HEADER_VISIBLESTATUS = ? WHERE TODO_HEADER_ID = ?"
        sql_params = (
            req.POST["GOAL_ID"],
            req.POST["TODO_HEADER_NAME"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_HEADER_STARTDATE"],
            req.POST["TODO_HEADER_ENDDATE"],
            req.POST["TODO_HEADER_VISIBLESTATUS"],
            TODO_HEADER_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_7, sql_params),
        }
        return JsonResponse(params)


def TODO_HEADER_DEL(req, TODO_HEADER_ID):
    if(req.method == 'POST'):
        sql_8 = "UPDATE T_TODO_HEADER SET TODO_HEADER_VISIBLESTATUS = ? WHERE TODO_HEADER_ID = ?"
        sql_params = (
            1, TODO_HEADER_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_8, sql_params),
        }
        return JsonResponse(params)
