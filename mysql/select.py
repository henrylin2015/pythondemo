#!/usr/bin/python3.4
# _*_ conding:utf-8 _*_
'''这是select pymysql'''
import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='python',port=3306,charset='utf8')
    #获取一个游标
    cur = conn.cursor()
    cur.execute('select * from users')
    data = cur.fetchall()
    print(data)
    cur.close()
    conn.close()
except Exception:
    print('发生错误了！')
