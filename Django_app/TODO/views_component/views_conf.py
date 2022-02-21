import datetime


# DBNAME = "DATABASE_DEV.DB"
DBNAME = "DATABASE_WK.DB"
#表示件数
sql_limit = 10
#非表示
visible = "0"
invisible = "1"
#表示文字数
len_character = 15
#現在時刻
nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
nowtime7 = (datetime.datetime.now()+datetime.timedelta(days=7)).strftime('%Y-%m-%d')
#null_par
null_par = "undefined"