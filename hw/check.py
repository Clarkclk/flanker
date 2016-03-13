from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import sys
import init

@csrf_exempt
def check(request):
    init.first()
    
    ans = "checkvalue"
    username = ''
    password = ''
    if request.POST.has_key('username'):
        username = str(request.POST['username'])
        password = str(request.POST['password'])
    
    fw = open('lol.txt', 'w')
    fw.write(username)
    fw.write(str(type(username)))
    fw.close()
    
    if(username != ''):
        try:
            conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
            cur=conn.cursor()
            cur.execute('create database if not exists python')
            conn.select_db('python')
            cur.execute('create table if not exists user(username varchar(20) primary key, password varchar(20))')
            cmd = 'select password FROM user where username = \'' + username + '\''
          #  cur.execute('select * from user')
            cur.execute(cmd)
            res = cur.fetchall()

           # fw = open('f.txt', 'w')
           # fw.write(username)
           # fw.write(password)
           # is_exist = 0
            for row in res:
               # print(row[0], row[1])
               # if((row[0] == username) and (row[1] == password)):
                if(row[0] == password):
                    ans = 'yes'
                    break
                
           # fw.close()
            conn.commit()
            cur.close()
            conn.close()
        
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #ans = 'yes'

    return render_to_response('loginpage.html', {'checkvalue': ans})
