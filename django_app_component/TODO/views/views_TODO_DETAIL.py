from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_limit = views_conf.sql_limit


def TODO_DETAIL_TOP(req, TODO_DETAIL_PAGE):
    sql_1 = "SELECT TODO_DETAIL_ID,TODO_HEADER_NAME,TODO_DETAIL_CONTENT,STATUS_NAME,TODO_DETAIL_DATE,TODO_HEADER_ENDDATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? "
    sql_1_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? "
    sql_1_option = ""
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    TODO_DETAIL_CONTENT = req.GET["TODO_DETAIL_CONTENT"]
    sql_params = [f"%{TODO_DETAIL_CONTENT}%", 0]
    sql_count_params = [f"%{TODO_DETAIL_CONTENT}%", 0]
    if(TODO_HEADER_ID != "0"):
        sql_1_option += "AND TODO_HEADER_ID = ? "
        sql_params.append(TODO_HEADER_ID)
        sql_count_params.append(TODO_HEADER_ID)
    sql_params.append(sql_limit)
    sql_params.append(sql_limit*(TODO_DETAIL_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY STATUS_ID,TODO_HEADER_ENDDATE,TODO_DETAIL_DATE DESC,TODO_DETAIL_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        "values_STATUS":views_COM.values_STATUS(),
    }
    return JsonResponse(params)


def TODO_DETAIL_TOP_DEL(req, TODO_DETAIL_PAGE):
    sql_1 = "SELECT TODO_DETAIL_ID,TODO_HEADER_NAME,TODO_DETAIL_CONTENT,STATUS_NAME,TODO_DETAIL_DATE,TODO_HEADER_ENDDATE FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? "
    sql_1_count = "SELECT COUNT(*) FROM V_TODO_DETAIL WHERE TODO_DETAIL_CONTENT LIKE ? AND TODO_DETAIL_VISIBLESTATUS = ? "
    sql_1_option = ""
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    TODO_DETAIL_CONTENT = req.GET["TODO_DETAIL_CONTENT"]
    sql_params = [f"%{TODO_DETAIL_CONTENT}%", 1]
    sql_count_params = [f"%{TODO_DETAIL_CONTENT}%", 1]
    if(TODO_HEADER_ID != "0"):
        sql_1_option += "AND TODO_HEADER_ID = ? "
        sql_params.append(TODO_HEADER_ID)
        sql_count_params.append(TODO_HEADER_ID)
    sql_params.append(sql_limit)
    sql_params.append(sql_limit*(TODO_DETAIL_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY STATUS_ID,TODO_HEADER_ENDDATE,TODO_DETAIL_DATE DESC,TODO_DETAIL_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        "values_STATUS":views_COM.values_STATUS(),
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
        sql_5 = "INSERT INTO T_TODO_DETAIL(TODO_HEADER_ID,TODO_DETAIL_CONTENT,STATUS_ID,TODO_DETAIL_DATE,TODO_DETAIL_VISIBLESTATUS) VALUES(?,?,?,?,?)"
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
        sql_6 = "SELECT TODO_DETAIL_ID,TODO_HEADER_ID,TODO_DETAIL_CONTENT,STATUS_ID,TODO_DETAIL_DATE,TODO_DETAIL_VISIBLESTATUS FROM T_TODO_DETAIL WHERE TODO_DETAIL_ID = ?"
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
        sql_7 = "UPDATE T_TODO_DETAIL SET TODO_HEADER_ID = ?,TODO_DETAIL_CONTENT = ?,STATUS_ID = ?,TODO_DETAIL_DATE = ?,TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
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
        sql_8 = "UPDATE T_TODO_DETAIL SET TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
        sql_params = (
            1, TODO_DETAIL_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_8, sql_params),
        }
        return JsonResponse(params)
