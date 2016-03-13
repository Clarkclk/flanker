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

class Task:
    def __init__(self,taskname,status):
        self.taskname=taskname
        self.status=status

@csrf_exempt
def index(request):
    
    init.first()
    try:
        buttonvalue = ''
        task = ''
        if request.POST.has_key('tasklist'):
            buttonvalue = str(request.POST['buttonvalue'])
            task = str(request.POST['tasklist'])

        if(buttonvalue == "delete"):
            database.execute('delete from tasklist where name = \'%s\'' % (task))
            database.execute('delete from edges where u = \'%s\' or v = \'%s\'' % (task,task))

        ss = str(request.path)
        site = ""

        if(buttonvalue == "modify"):
            site = "modifypage/%s" % (task)

        if(buttonvalue == "info"):
            site = "infopage/%s" % (task)
        
        if(buttonvalue == "presub"):
            site = "/prepage"
        
        if(buttonvalue == "start"):
            database.execute('update tasklist set status = \'started\' where name = \'%s\'' %task)
            init.checktask(task)
        #fw = open('listerr.txt','a')
        #fw.write(buttonvalue)
        #fw.write('\n python scheduler.py %s %s.sql\n' %(task,task))
        #fw.close()
        if(buttonvalue == "execute"):
            subprocess.Popen('python hw/scheduler.py %s %s.sql' %(task,task), shell = True)

            
        if(buttonvalue == "terminate"):
            res = database.getlist('select status from tasklist where name = \'%s\'' %task)[0]
            if res == 'started':
                database.execute('update tasklist set status = \'did not start\' where name = \'%s\'' %task)
            elif res == 'running':
                database.execute('update tasklist set status = \'failed\' where name = \'%s\'' %task)
            
        fw = open("log.txt","w")
        fw.write(site)
        fw.close()
        
        tasklist = database.getlist('select name from tasklist')
                    
        statuslist = database.getlist('select status from tasklist')

        ll = []
        for i in range(0,len(tasklist)):
            ll.append(Task(tasklist[i],statuslist[i]))

        return render_to_response('taskpage.html', {'tasklist': ll,'skipsite': site})
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        ferr = open("error.txt","w")
        ferr.write("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        ferr.close()
