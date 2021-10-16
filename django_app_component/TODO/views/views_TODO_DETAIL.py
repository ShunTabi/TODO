from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf

# 定義
sql_1 = "SELECT TODO_DETAIL_ID,GENRE_NAME,TODO_HEADER_NAME,TODO_DETAIL_NAME,PRIOR_SUBNAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE FROM V_TODO_DETAIL WHERE PRIOR_ID != (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_SUBNAME = ? ) AND (PRIOR_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?) ORDER BY TODO_DETAIL_ENDDATE,PRIOR_ID LIMIT ? OFFSET ?"
sql_1_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE PRIOR_ID != (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_SUBNAME = ? ) AND (PRIOR_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?)"
sql_2 = "SELECT TODO_DETAIL_ID,GENRE_NAME,TODO_HEADER_NAME,TODO_DETAIL_NAME,PRIOR_SUBNAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_ID NOT IN (SELECT TODO_DETAIL_ID FROM V_TODO_DETAIL WHERE (PRIOR_ID != (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_SUBNAME = ? )) OR (PRIOR_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?)) ORDER BY TODO_DETAIL_ENDDATE,PRIOR_ID LIMIT ? OFFSET ?"
sql_2_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_ID NOT IN (SELECT TODO_DETAIL_ID FROM V_TODO_DETAIL WHERE (PRIOR_ID != (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_SUBNAME = ? )) OR (PRIOR_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?))"
sql_3 = "SELECT TODO_DETAIL_ID,TODO_HEADER_NAME,TODO_DETAIL_NAME,PRIOR_NAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_ID = ?"
sql_4 = "SELECT GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_5 = "SELECT PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ?"
sql_6 = "INSERT INTO T_TODO_DETAIL(TODO_HEADER_ID,TODO_DETAIL_NAME,PRIOR_ID,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE) VALUES((SELECT TODO_HEADER_ID FROM T_TODO_HEADER WHERE TODO_HEADER_NAME = ?),?,(SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_NAME = ?),?,?)"
sql_7 = "UPDATE T_TODO_DETAIL SET TODO_HEADER_ID = (SELECT TODO_HEADER_ID FROM T_TODO_HEADER WHERE TODO_HEADER_NAME =?),PRIOR_ID = (SELECT PRIOR_ID FROM T_PRIOR WHERE PRIOR_NAME = ?),TODO_DETAIL_NAME = ?,TODO_DETAIL_STARTDATE = ?,TODO_DETAIL_ENDDATE = ? WHERE TODO_DETAIL_ID = ?"
sql_8 = "SELECT TODO_HEADER_NAME FROM T_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?"
sql_limit = views_conf.sql_limit


def TODO_DETAIL_TOP(req, TODO_DETAIL_PAGE):
    sql_params = (
        '済', 0, 0, 0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
    )
    sql_params_count = (
        '済', 0, 0, 0,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_params_count),
    }
    return JsonResponse(params)


def TODO_DETAIL_TOP_DEL(req, TODO_DETAIL_PAGE):
    sql_params = (
        '済', 0, 0, 1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
    )
    sql_params_count = (
        '済', 0, 0, 1,
    )
    params = {
        "values": views_SQL.SQL_SELECT(sql_2, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_2_count, sql_params_count),
    }
    return JsonResponse(params)


def TODO_DETAIL_FORM(req):
    if(req.method == "GET"):
        sql_params_PRIOR = (
            0,
        )
        sql_params_TODO_HEADER = (
            0,
        )
        params = {
            "values_PRIOR": views_SQL.SQL_SELECT(sql_5, sql_params_PRIOR),
            "values_TODO_HEADER": views_SQL.SQL_SELECT(sql_8, sql_params_TODO_HEADER)
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["PRIOR_NAME"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
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
        sql_params_PRIOR = (
            0,
        )
        sql_params_TODO_HEADER = (
            0,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_3, sql_params),
            "values_PRIOR": views_SQL.SQL_SELECT(sql_5, sql_params_PRIOR),
            "values_TODO_HEADER": views_SQL.SQL_SELECT(sql_8, sql_params_TODO_HEADER)
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_NAME"],
            req.POST["PRIOR_NAME"],
            req.POST["TODO_DETAIL_NAME"],
            req.POST["TODO_DETAIL_STARTDATE"],
            req.POST["TODO_DETAIL_ENDDATE"],
            TODO_DETAIL_ID,
        )
        print(sql_params)
        params = {
            "values": views_SQL.SQL_DCL(sql_7, sql_params),
        }
        return JsonResponse(params)
