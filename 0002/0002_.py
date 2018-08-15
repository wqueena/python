# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:12:30 2018

@author: queena
"""
import mysql.connector

connect = mysql.connector.connect(
    user='root', password='123456', host='localhost', database='testdb')
cursor = connect.cursor(buffered=True)


def ReadTxt():
    CodeList = []
    for line in open('0001.txt'):
        CodeList.append(str.replace(line, '\n', ''))
    return CodeList


def Create():
    sql_create = '''CREATE TABLE IF NOT EXISTS `code_table`(
                                                    `id` INT NOT NULL,
                                                    `code` VARCHAR(32) NOT NULL,
                                                    PRIMARY KEY(`id`)
                                                    )'''
    cursor.execute(sql_create)


def Insert(CodeList):
    i = 1
    sql_insert = 'insert into code_table (id,code) values (%s,%s)'
    for code in CodeList:
        data = (i, code)
        cursor.execute(sql_insert, data)
        i = i + 1
    connect.commit()
    cursor.execute('select * from test')
    for row in cursor.fetchall():
        print("id:%s\ncode:%s" % row)
    print(cursor.rowcount)
    cursor.close()
    connect.close()


if __name__ == '__main__':
    CodeList = ReadTxt()
    Create()
    Insert(CodeList)