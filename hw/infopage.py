#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import MySQLdb
import init


@csrf_exempt        
def index(request):
    init.first()
    
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        cur=conn.cursor()
        cur.execute('create database if not exists python')
        conn.select_db('python')
        cur.execute('create table if not exists tasklist(name varchar(125) primary key,type int,file varchar(100),status varchar(25),description varchar(2550))')

        name = ''
        if request.POST.has_key('taskname'):
            name = str(request.POST['taskname'])
            
        ss = request.path
        if name == '':
            name = ss[19:]
        cur.execute('select status from tasklist where name = \'%s\'' % (name))
        res = cur.fetchall()

        for i in res:
            for j in i:
                status = str(j)
                
        cur.execute('select description from tasklist where name = \'%s\'' % (name))
        res = cur.fetchall()

        for i in res:
            for j in i:
                description = str(j)

        fr = open("%s.sql" %(name),"r")
        code = fr.read()
        fr.close()
        conn.commit()
        cur.close()
        conn.close()
        return render_to_response('infopage.html', {'taskname': name,'taskstatus': status,'taskdescription': description,'taskcode': code})
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
