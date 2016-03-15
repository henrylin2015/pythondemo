#!/usr/bin/python3.4
# _*_  coding :utf-8 _*_

''' pymysql update '''
import pymysql
try:
    conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='python',port=3306,charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE `users` SET `name`= %s WHERE id=%s "
    cur.execute(sql,('test2','2'))
    conn.commit()
    cur.close()
    conn.close()
    print("update success")
except Exception:
    print("connection error!")
    
