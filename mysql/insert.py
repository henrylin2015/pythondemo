#!/usr/bin/python3.4
# _*_ coding : utf-8 _*_
import pymysql
"""pymysql insert """
try:
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='python',port=3306,charset='utf8')
    cur = conn.cursor()
    sql = "insert into `users`(`name`,`email`,`password`) values(%s,%s,%s)"
    cur.execute(sql,('web','web@admin.com','admin'))
    conn.commit()
    print("add success!")
    cur.close()
    conn.close()
except Exception:
    print("connection error")
