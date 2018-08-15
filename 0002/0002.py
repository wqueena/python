# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:04:49 2018

@author: queena
"""

import random
import string
import mysql.connector

length,count=16,200

ResultDic={}
Source=list(string.ascii_uppercase)
for index in range(0,10):
    Source.append(str(index))

connect = mysql.connector.connect(user='root', password='123456', host='localhost', database='testdb')
cursor=connect.cursor(buffered=True)

def create():
    sql_create='''CREATE TABLE IF NOT EXISTS `test`(
                                                    `id` INT NOT NULL,
                                                    `code` VARCHAR(32) NOT NULL,
                                                    PRIMARY KEY(`id`)
                                                    )'''
    cursor.execute(sql_create)

def insert():
    i=1
    while len(ResultDic)<count:
        code=''
        for index in range(0,length):
            code+=random.choice(Source)
        if code in ResultDic:
            pass
        else:
            ResultDic[code]=1
        sql_insert='insert into `test`(`id`,`code`) values(%s,"%s")'
        data=(i,code)
        cursor.execute(sql_insert,data)
        i=i+1
    connect.commit()
    sql='select * from test'
    cursor.execute(sql)
    for row in cursor.fetchall():
        print("id:%s\ncode:%s"%row)
    print(cursor.rowcount)
    cursor.close()
    connect.close()

if __name__=='__main__':
    create()
    insert()




