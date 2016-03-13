#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import MySQLdb
import database
import init


@csrf_exempt        
def index(request):
    init.first()
    
    try:

        name = ''
        ss = request.path
        if name == '':
            name = ss[21:]
                
        res = database.getlist('select description from tasklist where name = \'%s\'' % (name))
        description = res[0]

		
        ferr = open("error_modify.log","w")
        
        task = ''
        if request.POST.has_key('taskname'):
            task = str(request.POST['taskname'])

        ferr.write(r'-----%s' %(task))
        if task == name:
            code = str(request.POST['taskcode'])
            description = str(request.POST['taskdescription'])
            isModify = 'yes'
            fw = open("%s.sql" %(task),"w")
            fw.write(code)
            fw.close()
            database.execute('update tasklist set name = \'%s\', file = \'%s.sql\', description = \'%s\' where name = \'%s\'' %(task, task, description, name))
            database.execute('update edges set u = \'%s\' where u = \'%s\'' %(task, name))
            database.execute('update edges set v = \'%s\' where v = \'%s\'' %(task, name))
        else:
            task = name
            isModify = 'no'
            fr = open("%s.sql" %(name),"r")
            code = fr.read()
            fr.close()

        ferr.write(code)
        
        ferr.close()
        
        if request.POST.has_key('taskkind'):
            taskkind = str(request.POST['taskkind'])
            if taskkind == 'timed':
                hour = str(request.POST['hour'])
                minute = str(request.POST['minute'])
                database.execute('update tasklist set type = \'%s-%s\' where name = \'%s\'' %(hour, minute, task))
            else:
                database.execute('update tasklist set type = NULL where name = \'%s\'' %task )
            
        return render_to_response('modifypage.html', {'taskname': task,'modifystatus': isModify, 'taskdescription': description,'taskcode': code})
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
         return render_to_response('modifypage.html')
