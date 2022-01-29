import sqlite3
import json
from . import views_conf,views_setting_SQLSTATEMENT


def SQL_SELECT(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    # print(sql)
    # print("\n◆sqlパラメータ(SELECT)")
    # print(sql_params)
    cur.execute(sql, sql_params)
    output = cur.fetchall()
    # print("\n◆sql結果(SELECT)")
    # print(output)
    cur.close()
    conn.close()
    SQLLOG("1",sql,sql_params)
    return output


def SQL_DML(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    # print("\n◆sql(DML)")
    # print(sql)
    # print("\n◆sqlパラメータ(DML)")
    print(sql_params)
    cur.execute(sql, sql_params)
    cur.close()
    conn.commit()
    conn.close()
    SQLLOG("2",sql,sql_params)


def SQLLOG(code,sql,params):
    sql_params = (
        code,sql,json.dumps(params),
    )
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    cur.execute(views_setting_SQLSTATEMENT.sql_1001, sql_params)
    cur.close()
    conn.commit()
    conn.close()


def DEL_SQLLOG():
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    cur.execute(views_setting_SQLSTATEMENT.sql_1002)
    cur.close()
    conn.commit()
    conn.close()