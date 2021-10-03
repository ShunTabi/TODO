import sqlite3

DBNAME = "DATABASE.DB"
sql_limit = 8


def SQL_SELECT(sql, sql_params):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.execute(sql, sql_params)
    output = cur.fetchall()
    cur.close()
    conn.close()
    return output


def SQL_DCL(sql, sql_params):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.execute(sql, sql_params)
    cur.close()
    conn.commit()
    conn.close()
