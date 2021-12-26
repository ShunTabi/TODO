from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_limit = views_conf.sql_limit
sql_1 = "SELECT TODO_DETAIL_ID,TODO_HEADER_NAME,TODO_DETAIL_CONTENT,STATUS_NAME,TODO_DETAIL_DATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID,TODO_DETAIL_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT count(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? "
sql_2 = "SELECT TODO_DETAIL_ID,TODO_HEADER_NAME,TODO_DETAIL_CONTENT,STATUS_NAME,TODO_DETAIL_DATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_HEADER_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID,TODO_DETAIL_DATE DESC LIMIT ? OFFSET ?"
sql_2_count = "SELECT count(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_HEADER_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ?"
sql_5 = "INSERT INTO T_TODO_DETAIL(TODO_HEADER_ID,TODO_DETAIL_CONTENT,STATUS_ID,TODO_DETAIL_DATE,TODO_DETAIL_VISIBLESTATUS) VALUES(?,?,?,?,?)"
sql_6 = "SELECT TODO_DETAIL_ID,TODO_HEADER_ID,TODO_DETAIL_CONTENT,STATUS_ID,TODO_DETAIL_DATE,TODO_DETAIL_VISIBLESTATUS FROM T_TODO_DETAIL WHERE TODO_DETAIL_ID = ?"
sql_7 = "UPDATE T_TODO_DETAIL SET TODO_HEADER_ID = ?,TODO_DETAIL_CONTENT = ?,STATUS_ID = ?,TODO_DETAIL_DATE = ?,TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
sql_8 = "UPDATE T_TODO_DETAIL SET TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"


def TODO_DETAIL_TOP(req, TODO_DETAIL_PAGE):
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    TODO_DETAIL_CONTENT = req.GET["TODO_DETAIL_CONTENT"]
    if(TODO_HEADER_ID == "0"):
        sql_params = (
            f"%{TODO_DETAIL_CONTENT}%", 0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            f"%{TODO_DETAIL_CONTENT}%", 0,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_HEADER_ID != "0"):
        sql_params = (
            f"%{TODO_DETAIL_CONTENT}%", TODO_HEADER_ID, 0, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            f"%{TODO_DETAIL_CONTENT}%", TODO_HEADER_ID, 0,
        )
        sql = sql_2
        sql_count = sql_2_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        "values_STATUS":views_COM.values_STATUS(),
    }
    return JsonResponse(params)


def TODO_DETAIL_TOP_DEL(req, TODO_DETAIL_PAGE):
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    TODO_DETAIL_CONTENT = req.GET["TODO_DETAIL_CONTENT"]
    if(TODO_HEADER_ID == "0"):
        sql_params = (
            f"%{TODO_DETAIL_CONTENT}%", 1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            f"%{TODO_DETAIL_CONTENT}%", 1,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_HEADER_ID != "0"):
        sql_params = (
            f"%{TODO_DETAIL_CONTENT}%", TODO_HEADER_ID, 1, sql_limit, sql_limit*(TODO_DETAIL_PAGE-1),
        )
        sql_params_count = (
            f"%{TODO_DETAIL_CONTENT}%", TODO_HEADER_ID, 1,
        )
        sql = sql_2
        sql_count = sql_2_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
    }
    return JsonResponse(params)


def TODO_DETAIL_FORM(req):
    if(req.method == "GET"):
        params = {
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
            "values_STATUS": views_COM.values_STATUS()
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["TODO_DETAIL_CONTENT"],
            req.POST["STATUS_ID"],
            req.POST["TODO_DETAIL_DATE"],
            req.POST["TODO_DETAIL_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DML(sql_5, sql_params)
        }
        return JsonResponse(params)


def TODO_DETAIL_FORM_UPDATE(req, TODO_DETAIL_ID):
    if(req.method == "GET"):
        sql_params = (
            TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_6, sql_params),
            "values_TODO_HEADER":views_COM.values_TODO_HEADER(),
            "values_STATUS": views_COM.values_STATUS(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
            req.POST["TODO_DETAIL_CONTENT"],
            req.POST["STATUS_ID"],
            req.POST["TODO_DETAIL_DATE"],
            req.POST["TODO_DETAIL_VISIBLESTATUS"],
            TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_7, sql_params),
        }
        return JsonResponse(params)


def TODO_DETAIL_DEL(req, TODO_DETAIL_ID):
    if(req.method == 'POST'):
        sql_params = (
            1, TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_8, sql_params),
        }
        return JsonResponse(params)
