from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import subprocess
import MySQLdb
import sys
import os
import timevar
import init


@csrf_exempt
def work(request):
    init.first()
    
    code = ""
    buttonvalue = ""
    
    address = '127.0.0.1'
    sqlname = 'python'
    username = 'root'
    password = 'flanker'
    if(os.path.exists('config.txt')):
        fr = open("config.txt")
        list_of_all_the_lines = fr.readlines()
        address = list_of_all_the_lines[0][0:-1]
        sqlname = list_of_all_the_lines[1][0:-1]
        username = list_of_all_the_lines[2][0:-1]
        password = list_of_all_the_lines[3][0:-1]
        fr.close()
        
    if request.POST.has_key('hide'):
        code = str(request.POST['hide'])
        buttonvalue = str(request.POST['buttonvalue'])
        
    if(os.path.exists('load.sql')):
        fr = open('load.sql', 'r')
        code = fr.read()
        fr.close()
        os.system("rm -f load.sql")

    workvalue = 'workvalue'
    if(code != ''):
        fw = open('store.sql', 'w')
        fw.write("use %s;\n" %(sqlname))
        fw.write(timevar.timevar(code))
        fw.close()
    
    if(buttonvalue == "store"):
        workvalue = 'yes'
    
    result_store = ''
    if(buttonvalue == "execute"):
        #conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='flanker',port=3306)
        #cur=conn.cursor()
        #cur.execute('create database if not exists python')
        #conn.select_db('python')
        #cur.execute('create table if not exists user(username varchar(20) primary key, password varchar(20))')
        #cmd = 'mysql -h localhost -u root -pflanker < .\store.sql'
        #cur.execute(cmd)
        #conn.commit()
        #cur.close()
        #conn.close()
        
        cmd = "mysql -h localhost -u %s -p%s < store.sql > result_store.txt" %(username, password)
        temp = cmd.split()
        child = subprocess.Popen(cmd, shell = True)
        child.wait()
        if(os.path.exists('result_store.txt')):
            fr = open('result_store.txt','r')
            result_store = fr.read()
            fr.close()
                
    return render_to_response('workpage.html', {'workvalue' : workvalue, 'sqlname' : sqlname, 'code' : code, 'cons' : result_store})
    
