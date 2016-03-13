#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import MySQLdb
import re
import subprocess
import database
import init

@csrf_exempt
def index(request):
    init.first()
    
    if request.POST.has_key('taskname'):
        taskname = str(request.POST['taskname'])
        description = str(request.POST['taskdescription'])
        content = str(request.POST['taskcode'])
        fw = open("%s.sql" % taskname,"w")
        fw.write(content)
        fw.close()
            
            #fw.write("mysql -h localhost -u root -pflanker < %s.sql\n" %(taskname))
            #subprocess.Popen("chmod +x %s.sh" %(taskname), shell = True)
    else:
        taskname = ''
        description = ''
        content = ''
        
    if taskname == '':
        return render_to_response('addpage.html', {'taskname': taskname, 'taskdescription': description, 'sqlcode': content,'addstatus':'no'})

    
    try:
        database.execute('insert tasklist (name,file,status,description) values(\'%s\',\'%s.sql\',\'did not start\',\'%s\')' % (taskname, taskname, description))
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    taskkind = str(request.POST['taskkind'])
    if taskkind == 'timed':
        hour = str(request.POST['hour'])
        minute = str(request.POST['minute'])
        database.execute('update tasklist set type = \'%s-%s\' where name = \'%s\'' %(hour, minute, taskname))
    else:
        database.execute('update tasklist set type = NULL where name = \'%s\'' %taskname )
    return render_to_response('addpage.html', {'taskname': taskname, 'taskdescription': description, 'sqlcode': content,'addstatus':'yes'})
    
