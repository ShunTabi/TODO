from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views_SQL, views_conf, views_COM

# 定義
sql_limit = views_conf.sql_limit
sql_1 = "SELECT MEMO_ID,GOAL_NAME,TODO_HEADER_NAME,STATUS_NAME,TODO_DETAIL_CONTENT,MEMO_CONTENT,MEMO_DATE FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_1_count = "SELECT count(*) FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ?"
sql_2 = "SELECT MEMO_ID,GOAL_NAME,TODO_HEADER_NAME,STATUS_NAME,TODO_DETAIL_CONTENT,MEMO_CONTENT,MEMO_DATE FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND TODO_HEADER_ID = ? AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
sql_2_count = "SELECT count(*) FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND TODO_HEADER_ID = ? AND MEMO_VISIBLESTATUS = ?"
sql_5 = "INSERT INTO T_MEMO(TODO_HEADER_ID,TODO_DETAIL_ID,MEMO_CONTENT,MEMO_DATE,MEMO_VISIBLESTATUS) VALUES(?,?,?,?,?)"
sql_6 = "SELECT MEMO_ID,TODO_HEADER_ID,TODO_DETAIL_ID,MEMO_CONTENT,MEMO_DATE,MEMO_VISIBLESTATUS FROM V_MEMO WHERE MEMO_ID = ?"
sql_7 = "UPDATE T_MEMO SET TODO_HEADER_ID = ?,TODO_DETAIL_ID = ?,MEMO_CONTENT = ?,MEMO_DATE = ?,MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
sql_8 = "UPDATE T_MEMO SET MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"


def MEMO_TOP(req, MEMO_PAGE):
    sql_1 = "SELECT MEMO_ID,GOAL_NAME,TODO_HEADER_NAME,STATUS_NAME,TODO_DETAIL_CONTENT,MEMO_CONTENT,MEMO_DATE FROM V_MEMO WHERE (TODO_DETAIL_CONTENT LIKE ? OR MEMO_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_count = "SELECT count(*) FROM V_MEMO WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_CONTENT LIKE ?) AND MEMO_VISIBLESTATUS = ? "
    sql_1_option = ""
    GOAL_ID = req.GET["GOAL_ID"]
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    MEMO_CONTENT = req.GET["value_MEMO_CONTENT"]
    sql_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", 0]
    sql_count_params = [f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", 0]
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
    sql_1 += sql_1_option + "ORDER BY MEMO_DATE DESC LIMIT ? OFFSET ?"
    sql_1_count += sql_1_option
    print(TODO_HEADER_ID)
    print(req.GET["GOAL_ID"])
    TODO_HEADER_ID = int(TODO_HEADER_ID)
    GOAL_ID = int(GOAL_ID)
    params = {
        "values": views_SQL.SQL_SELECT(sql_1, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_1_count, sql_count_params),
        "values_TODO_HEADER":views_COM.values_TODO_HEADER2(GOAL_ID),
        "values_GOAL":views_COM.values_GOAL(),
        "GOAL_ID":views_COM.values_GOAL2(GOAL_ID,TODO_HEADER_ID),
    }
    return JsonResponse(params)


def MEMO_TOP_DEL(req, MEMO_PAGE):
    GOAL_ID = int(req.GET["GOAL_ID"])
    MEMO_CONTENT = req.GET["value_MEMO_CONTENT"]
    TODO_HEADER_ID = req.GET["TODO_HEADER_ID"]
    if(TODO_HEADER_ID == "0"):
        sql_params = (
            f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", 1,sql_limit, sql_limit*(MEMO_PAGE-1),
        )
        sql_params_count = (
            f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%", 1,
        )
        sql = sql_1
        sql_count = sql_1_count
    elif(TODO_HEADER_ID != "0"):
        sql_params = (
            f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%",TODO_HEADER_ID, 0,sql_limit, sql_limit*(MEMO_PAGE-1),
        )
        sql_params_count = (
            f"%{MEMO_CONTENT}%",f"%{MEMO_CONTENT}%",TODO_HEADER_ID, 0,
        )
        sql = sql_2
        sql_count = sql_2_count
    params = {
        "values": views_SQL.SQL_SELECT(sql, sql_params),
        "values_COUNT": views_SQL.SQL_SELECT(sql_count, sql_params_count),
        "values_TODO_HEADER":views_COM.values_TODO_HEADER2(int(GOAL_ID)),
        "values_GOAL":views_COM.values_GOAL(),
        # "GOAL_ID":views_COM.values_GOAL2(int(TODO_HEADER_ID)),
    }
    return JsonResponse(params)


def MEMO_FORM(req):
    if(req.method == "GET"):
        TODO_HEADER_ID = int(req.GET["TODO_HEADER_ID"])
        params = {
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL2(TODO_HEADER_ID),
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        }
        return JsonResponse(params)
    elif(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
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
        TODO_HEADER_ID = int(req.GET["TODO_HEADER_ID"])
        sql_params = (
            MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_SELECT(sql_6, sql_params),
            "values_TODO_DETAIL": views_COM.values_TODO_DETAIL2(TODO_HEADER_ID),
            "values_TODO_HEADER": views_COM.values_TODO_HEADER(),
        }
        return JsonResponse(params)
    if(req.method == "POST"):
        sql_params = (
            req.POST["TODO_HEADER_ID"],
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
        sql_params = (
            1, MEMO_ID,
        )
        params = {
            "values": views_SQL.SQL_DML(sql_8, sql_params),
        }
        return JsonResponse(params)
