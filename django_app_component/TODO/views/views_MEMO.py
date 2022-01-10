from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_limit = views_conf.sql_limit


def MEMO_TOP(req, MEMO_PAGE):
    sql_1 = "SELECT MEMO_ID,GOAL_NAME,TODO_HEADER_NAME,STATUS_NAME,TODO_DETAIL_CONTENT,MEMO_CONTENT,MEMO_DATE FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_count = "SELECT count(*) FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_option = ""
    GOAL_ID = req.GET["GOAL_ID"]
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    MEMO_CONTENT = req.GET["value_MEMO_CONTENT"]
    sql_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", "0"]
    sql_count_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", "0"]
    if(GOAL_ID != "0"):
        sql_1_option += "AND GOAL_ID = ? "
        sql_params.append(GOAL_ID)
        sql_count_params.append(GOAL_ID)
    if(TODO_HEADER_ID != "0"):
        sql_1_option += "AND TODO_HEADER_ID = ? "
        sql_params.append(TODO_HEADER_ID)
        sql_count_params.append(TODO_HEADER_ID)
    sql_params.append(sql_limit)
    sql_params.append(sql_limit*(MEMO_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY MEMO_DATE DESC,MEMO_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_GOAL":views_COM.values_GOAL(),
        "values_TODO_HEADER":views_COM.values_TODO_HEADER2(GOAL_ID),
    }
    return JsonResponse(params)


def MEMO_TOP_DEL(req, MEMO_PAGE):
    sql_1 = "SELECT MEMO_ID,GOAL_NAME,TODO_HEADER_NAME,STATUS_NAME,TODO_DETAIL_CONTENT,MEMO_CONTENT,MEMO_DATE FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_count = "SELECT count(*) FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_option = ""
    GOAL_ID = req.GET["GOAL_ID"]
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    MEMO_CONTENT = req.GET["value_MEMO_CONTENT"]
    sql_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", "1"]
    sql_count_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", "1"]
    if(GOAL_ID != "0"):
        sql_1_option += "AND GOAL_ID = ? "
        sql_params.append(GOAL_ID)
        sql_count_params.append(GOAL_ID)
    if(TODO_HEADER_ID != "0"):
        sql_1_option += "AND TODO_HEADER_ID = ? "
        sql_params.append(TODO_HEADER_ID)
        sql_count_params.append(TODO_HEADER_ID)
    sql_params.append(sql_limit)
    sql_params.append(sql_limit*(MEMO_PAGE-1))
    sql_1 += sql_1_option + "ORDER BY MEMO_DATE DESC,MEMO_ID DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_GOAL":views_COM.values_GOAL(),
        "values_TODO_HEADER":views_COM.values_TODO_HEADER2(GOAL_ID),
    }
    return JsonResponse(params)


def MEMO_FORM(req):
    if(req.method == "GET"):
        TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
        params = {
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL2(TODO_HEADER_ID),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_5 = "INSERT INTO T_MEMO(TODO_DETAIL_ID,MEMO_CONTENT,MEMO_DATE,MEMO_VISIBLESTATUS) VALUES(?,?,?,?)"
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_CONTENT"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
        )
        params = {
            "values": views_SQL.SQL_DML(sql_5, sql_params)
        }
        return JsonResponse(params)


def MEMO_FORM_UPDATE(req, MEMO_ID):
    if(req.method == "GET"):
        sql_6 = "SELECT MEMO_ID,TODO_HEADER_ID,TODO_DETAIL_ID,MEMO_CONTENT,MEMO_DATE,MEMO_VISIBLESTATUS FROM V_MEMO WHERE MEMO_ID = ?"
        sql_params = (
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_6, sql_params),
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL(),
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_7 = "UPDATE T_MEMO SET TODO_DETAIL_ID = ?,MEMO_CONTENT = ?,MEMO_DATE = ?,MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
        sql_params = (
            req.POST["TODO_DETAIL_ID"],
            req.POST["MEMO_CONTENT"],
            req.POST["MEMO_DATE"],
            req.POST["MEMO_VISIBLESTATUS"],
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_7, sql_params),
        }
        return JsonResponse(params)


def MEMO_DEL(req, MEMO_ID):
    if(req.method == 'POST'):
        sql_8 = "UPDATE T_MEMO SET MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
        sql_params = (
            "1", MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_8, sql_params),
        }
        return JsonResponse(params)
