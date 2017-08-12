#!/usr/bin/python
#coding=utf-8

import MySQLdb

import getpass
password = getpass.getpass("Please input your password:")

try:
    db = MySQLdb.connect('localhost','root',password,'stu')
except MySQLdb.OperationalError:
    exit(1)


cursor = db.cursor()
try:
    cursor.execute("select * from student")
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data

    data = cursor.fetchall()
    # print data
#打印出字段名
    for i in cursor.description:
        print i[0],

    print ""
#打印出每条信息
    for row in data:
        for i in row:
            print i,
        print ""
except:
    print "Error:unable to fecth data"

db.close()
