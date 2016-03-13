#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import MySQLdb
import re
import os
import database
import init
import newtask
import thread
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


@csrf_exempt
def show(request):
    
    init.first()
    try:
        task = ''
        res = ''
        if request.POST.has_key('tasklist'):
            task = str(request.POST['tasklist'])
            fw = open('result_store.sql','w')
            fw.write('use python;\n')
            fw.write('select * from %s;\n' % task)
            fw.close()
            cmd = "mysql -h localhost -u root -pflanker < result_store.sql > result_store.res"
            child = subprocess.Popen(cmd, shell = True)
            child.wait()
            fr = open('result_store.res','r')
            res = fr.read()
            fr.close()

        ll = database.getlist('show tables')
        return render_to_response('showpage.html', {'tasklist': ll,'cons': res})
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        ferr = open("error.txt","w")
        ferr.write("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        ferr.close()
