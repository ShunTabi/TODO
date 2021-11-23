from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_1 = "SELECT TODO_DETAIL_ID,GENRE_SUBNAME,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,PRIOR_SUBNAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE,TODO_DETAIL_VISIBLESTATUS FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ? ORDER BY PRIOR_ID,TODO_DETAIL_ENDDATE,TODO_DETAIL_STARTDATE LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ?"
sql_2 = "SELECT TODO_DETAIL_ID,GENRE_SUBNAME,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,PRIOR_SUBNAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE,TODO_DETAIL_VISIBLESTATUS FROM V_TODO_DETAIL WHERE PRIOR_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY PRIOR_ID,TODO_DETAIL_ENDDATE,TODO_DETAIL_STARTDATE LIMIT ? OFFSET ?"
sql_2_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE PRIOR_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ?"
sql_4 = "SELECT TODO_DETAIL_ID,GENRE_SUBNAME,TODO_HEADER_SUBNAME,TODO_DETAIL_NAME,PRIOR_SUBNAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE,TODO_DETAIL_VISIBLESTATUS FROM V_TODO_DETAIL WHERE TODO_HEADER_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY PRIOR_ID,TODO_DETAIL_ENDDATE,TODO_DETAIL_STARTDATE LIMIT ? OFFSET ?"
sql_4_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE TODO_HEADER_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ?"
sql_3 = "SELECT TODO_DETAIL_ID,TODO_HEADER_ID,TODO_DETAIL_NAME,PRIOR_ID,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE,TODO_DETAIL_VISIBLESTATUS FROM V_TODO_DETAIL WHERE TODO_DETAIL_ID = ?"
sql_6 = "INSERT INTO T_TODO_DETAIL(TODO_HEADER_ID,TODO_DETAIL_NAME,PRIOR_ID,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE,TODO_DETAIL_VISIBLESTATUS) VALUES(?,?,?,?,?,?)"
sql_7 = "UPDATE T_TODO_DETAIL SET TODO_HEADER_ID = ?,TODO_DETAIL_NAME = ?,PRIOR_ID = ?,TODO_DETAIL_STARTDATE = ?,TODO_DETAIL_ENDDATE = ?,TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
sql_9 = "UPDATE T_TODO_DETAIL SET TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
sql_limit = views_conf.sql_limit


def TODO_DETAIL_TOP(req, TODO_DETAIL_PAGE):
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    PRIOR_ID = req.GET["PRIOR_ID"]
    if(TODO_HEADER_ID == "0" and PRIOR_ID == "0"):
        sql_params = (
            0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            0,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_HEADER_ID == "0" and PRIOR_ID != "0"):
        sql_params = (
            PRIOR_ID, 0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            PRIOR_ID, 0,
        )
        sql = sql_2
        sql_count = sql_2_count
    elif(TODO_HEADER_ID != "0" and PRIOR_ID == "0"):
        sql_params = (
            TODO_HEADER_ID, 0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            TODO_HEADER_ID, 0,
        )
        sql = sql_4
        sql_count = sql_4_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        "values_PRIOR": views_COM.values_PRIOR(),
    }
    return JsonResponse(params)


def TODO_DETAIL_TOP_DEL(req, TODO_DETAIL_PAGE):
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    PRIOR_ID = req.GET["PRIOR_ID"]
    if(TODO_HEADER_ID == "0" and PRIOR_ID == "0"):
        sql_params = (
            1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            1,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_HEADER_ID == "0" and PRIOR_ID != "0"):
        sql_params = (
            PRIOR_ID, 1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            PRIOR_ID, 1,
        )
        sql = sql_2
        sql_count = sql_2_count
    elif(TODO_HEADER_ID != "0" and PRIOR_ID == "0"):
        sql_params = (
            TODO_HEADER_ID, 1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            TODO_HEADER_ID, 1,
        )
        sql = sql_4
        sql_count = sql_4_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        "values_PRIOR": views_COM.values_PRIOR(),
    }
    return JsonResponse(params)


def TODO_DETAIL_FORM(req):
    if(req.method == "GET"):
        params = {
            "values_PRIOR": views_COM.values_PRIOR(),
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
            req.POST["TODO_DETAIL_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_6, sql_params),
        }
        return JsonResponse(params)


def TODO_DETAIL_FORM_UPDATE(req, TODO_DETAIL_ID):
    if(req.method == "GET"):
        sql_params = (
            TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_3, sql_params),
            "values_PRIOR": views_COM.values_PRIOR(),
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["PRIOR_ID"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
            req.POST["TODO_DETAIL_VISIBLESTATUS"],
            TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_7, sql_params),
        }
        return JsonResponse(params)


def TODO_DETAIL_DEL(req, TODO_DETAIL_ID):
    if(req.method == 'POST'):
        sql_params = (
            1, TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_DCL(sql_9, sql_params),
        }
        return JsonResponse(params)
