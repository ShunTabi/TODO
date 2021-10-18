import sqlite3
from . import views_conf


def SQL_SELECT(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    cur.execute(sql, sql_params)
    output = cur.fetchall()
    cur.close()
    conn.close()
    return output


def SQL_DCL(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    cur.execute(sql, sql_params)
    cur.close()
    conn.commit()
    conn.close()
