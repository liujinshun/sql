#!/usr/bin/python
#coding=utf-8

import MySQLdb
#密文输入
import getpass
password = getpass.getpass("Please input your password:")
#打开数据库链接
try:
    db = MySQLdb.connect('localhost','root',password,'stu')
except MySQLdb.OperationalError:
    exit(1)

#获取数据库游标
cursor = db.cursor()


#执行数据库sql语句
cursor.execute("select version()")

#得到语句执行结果
data = cursor.fetchone()

print "database : ",data
#如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("drop table if exists newtab")
## 创建数据表
sql = '''create table newtab (first_name char(20) not null,
         last_name char(20),
         age int,
         sex char(2)
         )'''
cursor.execute(sql)
# SQL 插入语句
sql = "insert into newtab values ('Mac','Mohan',20,'M')"

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except MySQLdb.ProgrammingError:
    db.rollback()

sql = "delete from newtab where age > 20"

try:
    cursor.execute(sql)
    db.commit()
except MySQLdb.ProgrammingError:
    db.rollback()



db.close()
