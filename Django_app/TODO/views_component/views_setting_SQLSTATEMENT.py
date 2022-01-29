from . import views_conf


item_GENRE = "GENRE_NAME"
item_GOAL = "GENRE_ID,GOAL_NAME"
item_TODO_HEADER = "GOAL_ID,PRIOR_ID,TODO_HEADER_NAME,TODO_HEADER_ENDDATE"
item_TODO_DETAIL = "TODO_HEADER_ID,STATUS_ID,TODO_DETAIL_NAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE"
item_MEMO = "TODO_DETAIL_ID,MEMO_CONTENT"
#GENRE
sql_11_1 = "SELECT GENRE_ID,GENRE_NAME,STRFTIME('%Y-%m-%d',GENRE_DATETIME) FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ? ORDER BY GENRE_DATETIME DESC LIMIT ? OFFSET ?"
sql_11_2 = "SELECT COUNT(*) FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ?"
sql_12 = f"INSERT INTO T_GENRE({item_GENRE}) VALUES(?)"
sql_13 = f"SELECT GENRE_ID,{item_GENRE} FROM T_GENRE WHERE GENRE_ID = ?"
sql_14 = f"UPDATE T_GENRE SET ({item_GENRE},GENRE_DATETIME) = (?,CURRENT_TIMESTAMP) WHERE GENRE_ID = ?"
sql_15 = "UPDATE T_GENRE SET GENRE_VISIBLESTATUS = ? WHERE GENRE_ID = ?"
sql_19 = "SELECT GENRE_ID,GENRE_NAME FROM T_GENRE WHERE GENRE_VISIBLESTATUS = ? ORDER BY GENRE_NAME"
#GOAL
sql_21_1 = "SELECT GOAL_ID,GENRE_NAME,GOAL_NAME,STRFTIME('%Y-%m-%d',GOAL_DATETIME) FROM V_GOAL WHERE GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? ORDER BY GOAL_DATETIME LIMIT ? OFFSET ?"
sql_21_2 = "SELECT COUNT(*) FROM V_GOAL WHERE GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ?"
sql_22 = f"INSERT INTO T_GOAL({item_GOAL}) VALUES(?,?)"
sql_23 = f"SELECT GOAL_ID,{item_GOAL} FROM T_GOAL WHERE GOAL_ID = ?"
sql_24 = f"UPDATE T_GOAL SET ({item_GOAL},GOAL_DATETIME) = (?,?,CURRENT_TIMESTAMP) WHERE GOAL_ID = ?"
sql_25 = "UPDATE T_GOAL SET GOAL_VISIBLESTATUS = ? WHERE GOAL_ID = ?"
sql_29 = f"SELECT GOAL_ID,SUBSTR(GOAL_NAME,1,{views_conf.len_character}) FROM T_GOAL WHERE GOAL_VISIBLESTATUS = ? ORDER BY GOAL_NAME"
#TODO_HEADER
sql_31_1 = "SELECT TODO_HEADER_ID,GENRE_NAME,GOAL_NAME,TODO_HEADER_NAME,PRIOR_NAME,TODO_HEADER_ENDDATE FROM V_TODO_HEADER \
    WHERE TODO_HEADER_NAME LIKE ? AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? ORDER BY TODO_HEADER_DATETIME DESC LIMIT ? OFFSET ?"
sql_31_2 = "SELECT COUNT(*) FROM V_TODO_HEADER WHERE TODO_HEADER_NAME LIKE ? AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ?"
sql_32 = f"INSERT INTO T_TODO_HEADER({item_TODO_HEADER}) VALUES(?,?,?,?)"
sql_33 = f"SELECT TODO_HEADER_ID,{item_TODO_HEADER} FROM T_TODO_HEADER WHERE TODO_HEADER_ID = ?"
sql_34 = f"UPDATE T_TODO_HEADER SET ({item_TODO_HEADER},TODO_HEADER_DATETIME) = (?,?,?,?,CURRENT_TIMESTAMP) WHERE TODO_HEADER_ID = ?"
sql_35 = "UPDATE T_TODO_HEADER SET TODO_HEADER_VISIBLESTATUS = ? WHERE TODO_HEADER_ID = ?"
sql_39_1 = f"SELECT TODO_HEADER_ID,SUBSTR(TODO_HEADER_NAME,1,{views_conf.len_character}) FROM T_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ?"
sql_39_2 = f"SELECT TODO_HEADER_ID,SUBSTR(TODO_HEADER_NAME,1,{views_conf.len_character}) FROM T_TODO_HEADER WHERE TODO_HEADER_VISIBLESTATUS = ? AND GOAL_ID = ?"
#TODO_DETAIL
sql_41_1_1 = "SELECT TODO_DETAIL_ID,GENRE_NAME,GOAL_NAME,TODO_HEADER_NAME,TODO_DETAIL_NAME,STATUS_NAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE FROM V_TODO_DETAIL \
    WHERE (TODO_HEADER_NAME LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID,TODO_DETAIL_DATETIME DESC LIMIT ? OFFSET ?"
sql_41_1_2 = "SELECT TODO_DETAIL_ID,GENRE_NAME,GOAL_NAME,TODO_HEADER_NAME,TODO_DETAIL_NAME,STATUS_NAME,TODO_DETAIL_STARTDATE,TODO_DETAIL_ENDDATE FROM V_TODO_DETAIL \
    WHERE (TODO_HEADER_NAME LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND STATUS_ID = ? AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ? ORDER BY STATUS_ID,TODO_DETAIL_DATETIME DESC LIMIT ? OFFSET ?"
sql_41_2_1 = "SELECT COUNT(*) FROM V_TODO_DETAIL \
    WHERE (TODO_HEADER_NAME LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?"
sql_41_2_2 = "SELECT COUNT(*) FROM V_TODO_DETAIL \
    WHERE (TODO_HEADER_NAME LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND STATUS_ID = ? AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ?"
sql_42 = f"INSERT INTO T_TODO_DETAIL({item_TODO_DETAIL}) VALUES(?,?,?,?,?)"
sql_43 = f"SELECT TODO_DETAIL_ID,{item_TODO_DETAIL} FROM T_TODO_DETAIL WHERE TODO_DETAIL_ID = ?"
sql_44 = f"UPDATE T_TODO_DETAIL SET ({item_TODO_DETAIL},TODO_DETAIL_DATETIME) = (?,?,?,?,?,CURRENT_TIMESTAMP) WHERE TODO_DETAIL_ID = ?"
sql_45 = "UPDATE T_TODO_DETAIL SET TODO_DETAIL_VISIBLESTATUS = ? WHERE TODO_DETAIL_ID = ?"
sql_49_1 = f"SELECT TODO_DETAIL_ID,SUBSTR(TODO_DETAIL_NAME,1,{views_conf.len_character}),SUBSTR(STATUS_NAME,1,{views_conf.len_character}) FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ?"
sql_49_2 = f"SELECT TODO_DETAIL_ID,SUBSTR(TODO_DETAIL_NAME,1,{views_conf.len_character}),SUBSTR(STATUS_NAME,1,{views_conf.len_character}) FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ? AND GOAL_ID = ?"
sql_49_3 = f"SELECT TODO_DETAIL_ID,TODO_DETAIL_ID,SUBSTR(TODO_DETAIL_NAME,1,{views_conf.len_character}),SUBSTR(STATUS_NAME,1,{views_conf.len_character}) FROM V_TODO_DETAIL WHERE TODO_DETAIL_VISIBLESTATUS = ? AND TODO_HEADER_ID = ?"
#MEMO
sql_51_1 = "SELECT MEMO_ID,GENRE_NAME,GOAL_NAME,TODO_HEADER_NAME,TODO_DETAIL_NAME,STATUS_NAME,MEMO_CONTENT,STRFTIME('%Y-%m-%d',MEMO_DATETIME) FROM V_MEMO \
    WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ? AND MEMO_VISIBLESTATUS = ? ORDER BY MEMO_DATETIME DESC LIMIT ? OFFSET ?"
sql_51_2 = "SELECT COUNT(*) FROM V_MEMO \
    WHERE (MEMO_CONTENT LIKE ? OR TODO_DETAIL_NAME LIKE ?) AND GENRE_VISIBLESTATUS = ? AND GOAL_VISIBLESTATUS = ? AND TODO_HEADER_VISIBLESTATUS = ? AND TODO_DETAIL_VISIBLESTATUS = ? AND MEMO_VISIBLESTATUS = ?"
sql_52 = f"INSERT INTO T_MEMO({item_MEMO}) VALUES(?,?)"
sql_53 = f"SELECT MEMO_ID,{item_MEMO} FROM T_MEMO WHERE MEMO_ID = ?"
sql_54 = f"UPDATE T_MEMO SET ({item_MEMO},MEMO_DATETIME) = (?,?,CURRENT_TIMESTAMP) WHERE MEMO_ID = ?"
sql_55 = "UPDATE T_MEMO SET MEMO_VISIBLESTATUS = ? WHERE MEMO_ID = ?"
#PRIOR
sql_61 = "SELECT PRIOR_ID,PRIOR_NAME FROM T_PRIOR WHERE PRIOR_VISIBLESTATUS = ? ORDER BY PRIOR_ID"
#STATUS
sql_62 = "SELECT STATUS_ID,STATUS_NAME FROM T_STATUS WHERE STATUS_VISIBLESTATUS = ? ORDER BY STATUS_ID"


#SQLLOG
sql_1001 = "INSERT INTO T_SQLLOG(SQLLOG_CODE,SQLLOG_SQLSTATEMENT,SQLLOG_PAR) VALUES(?,?,?)"
sql_1002 = "DELETE FROM T_SQLLOG"