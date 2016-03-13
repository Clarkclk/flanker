 #coding=utf-8
import MySQLdb
import re
import os
import sys, urllib


def init():
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur = conn.cursor()
        cur.execute('create database if not exists python')
        conn.select_db('python')
        cur.execute('create table if not exists tasklist(name varchar(125) primary key,type varchar(100),file varchar(100),status varchar(25),description varchar(2550))')
        cur.execute('create table if not exists edges (u varchar(125),v varchar(125))')
        cur.execute('create table if not exists user(username varchar(20) primary key, password varchar(20))')
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def execute(command):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur = conn.cursor()
        conn.select_db('python')
        cur.execute(command)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getlist(command):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur = conn.cursor()
        conn.select_db('python')
        cur.execute(command)
        res = cur.fetchall()
        
        result = []
        for i in res:
            for j in i:
                result.append(j)
                
        conn.commit()
        cur.close()
        conn.close()
        
        return result
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return []

def delete(taskName):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur = conn.cursor()
        conn.select_db('python')
        cur.execute('delete from tasklist where name = \'%s\'' % (taskName))
        cur.execute('delete from edges where u = \'%s\' or v = \'%s\'' % (taskName,taskName))
                
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def modify(oldName, newName, description):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur = conn.cursor()
        conn.select_db('python')
        cur.execute(command)
        cur.execute('update tasklist set name = \'%s\', file = \'%s.sql\', description = \'%s\' where name = \'%s\'' %(newName, newName, description, oldName))
        cur.execute('update edges set u = \'%s\' where u = \'%s\'' %(newName, oldName))
        cur.execute('update edges set v = \'%s\' where v = \'%s\'' %(newName, oldName))
        conn.commit()
        cur.close()
        conn.close()
        
        return result
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return []