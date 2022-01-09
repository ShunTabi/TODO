from . import views_SQL

# STATUS
#TODO_DETAIL



def values_GENRE():
    sql_1 = "SELECT GENRE_ID,GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_1, sql_params)
    return result


def values_PRIOR():
    sql_2 = "SELECT PRIOR_ID,PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ?"
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_2, sql_params)
    return result


def values_GOAL():
    sql_3 = "SELECT GOAL_ID,GOAL_NAME FROM V_GOAL WHERE GOAL_VISIBLESTATUS = ?"
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_3,sql_params)
    return result


def values_TODO_HEADER():
    sql_4 = "SELECT TODO_HEADER_ID,TODO_HEADER_NAME FROM V_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?"
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_4, sql_params)
    return result


def values_TODO_HEADER2(GOAL_ID):
    if(GOAL_ID == 0):
        return values_TODO_HEADER()
    elif(GOAL_ID != 0):
        sql_5 = "SELECT TODO_HEADER_ID,TODO_HEADER_NAME FROM V_TODO_HEADER WHERE GOAL_ID = ? AND TODO_HEADER_VISIBLESTATUS = ?"
        sql_params = (
            GOAL_ID,0
        )
        result = views_SQL.SQL_SELECT(sql_5, sql_params)
        return result


def values_STATUS():
    sql_6 = "SELECT STATUS_ID,STATUS_NAME FROM T_STATUS WHERE STATUS_VISIBLESTATUS = ?"
    sql_params = (
        0,
    )
    result = views_SQL.SQL_SELECT(sql_6, sql_params)
    return result


def values_TODO_DETAIL():
    sql_8 = "SELECT TODO_DETAIL_ID,STATUS_NAME,SUBSTR(TODO_DETAIL_CONTENT,1,?) FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID"
    sql_params = (
        views_conf.len_character,0,
    )
    result = views_SQL.SQL_SELECT(sql_8, sql_params)
    return result
def values_TODO_DETAIL2(TODO_HEADER_ID):
    sql_9 = "SELECT TODO_DETAIL_ID,STATUS_NAME,SUBSTR(TODO_DETAIL_CONTENT,1,?) FROM V_TODO_DETAIL WHERE TODO_HEADER_ID = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID"
    if(TODO_HEADER_ID == 0):
        
        return values_TODO_DETAIL()
    elif(TODO_HEADER_ID != 0):
        sql_params = (
            views_conf.len_character,TODO_HEADER_ID,0
        )
        result = views_SQL.SQL_SELECT(sql_9, sql_params)
        return result

