import sqlite3
from . import views_conf


def SQL_SELECT(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    print("\n◆sql(SELECT)")
    print(sql)
    print("\n◆sqlパラメータ(SELECT)")
    print(sql_params)
    cur.execute(sql, sql_params)
    output = cur.fetchall()
    print("\n◆sql結果(SELECT)")
    print(output)
    cur.close()
    conn.close()
    return output


def SQL_DML(sql, sql_params):
    conn = sqlite3.connect(views_conf.DBNAME)
    cur = conn.cursor()
    print("\n◆sql(DML)")
    print(sql)
    print("\n◆sqlパラメータ(DML)")
    print(sql_params)
    cur.execute(sql, sql_params)
    cur.close()
    conn.commit()
    conn.close()
