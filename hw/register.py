from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import sys
import init

@csrf_exempt
def register(request):
    init.first()
    
    username = ''
    password = ''
    ans = 'checkvalue'
    if request.POST.has_key('username'):
        username = str(request.POST['username'])
        password = str(request.POST['password'])

    fw = open('re.txt', 'a')
    fw.write("lol")
    fw.write(username)
    fw.write(password)
    fw.close()
    
    if(username != ''):
        try:
            conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
            cur=conn.cursor()
            cur.execute('create database if not exists python')
            conn.select_db('python')
            cur.execute('create table if not exists user(username varchar(20) primary key, password varchar(20))')
            cur.execute('select username from user')
            res = cur.fetchall()

            fw = open('re.txt', 'w')
            fw.write(username)
            fw.write(password)
            fw.write("lala")
            ans = "yes"
            for row in res:
                fw.write(row[0])
                fw.write("  ")
                fw.write(ans)
                if(row[0] == username):
                    ans = "no"
                    break

            cmd = "INSERT INTO user(username, password) VALUES(\'" + username + "\', \'" + password + "\')"
            if(ans == "yes"):
                fw.write("execute")
                cur.execute(cmd)

            fw.write(ans)
            fw.close()
            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    return render_to_response('registerpage.html', {'checkvalue': ans})
