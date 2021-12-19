from . import views_SQL

# 定義
# GENRE
sql_1 = "SELECT GENRE_ID,GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
# PRIOR
sql_2 = "SELECT PRIOR_ID,PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ?"
# GOAL
sql_3 = "SELECT GOAL_ID,GOAL_NAME FROM V_GOAL WHERE GOAL_VISIBLESTATUS = ?"
# TODO_HEADER
sql_4 = "SELECT TODO_HEADER_ID,TODO_HEADER_NAME FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?"
# STATUS
sql_5 = "SELECT STATUS_ID,STATUS_NAME FROM T_STATUS WHERE STATUS_VISIBLESTATUS = ?"



def values_GENRE():
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_1, sql_params)
    return result


def values_PRIOR():
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_2, sql_params)
    return result


def values_GOAL():
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_3,sql_params)
    return result


def values_TODO_HEADER():
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_4, sql_params)
    return result

def values_STATUS():
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_5, sql_params)
    return result