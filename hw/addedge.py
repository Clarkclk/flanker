#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import MySQLdb
import re
import os
import sys, urllib
import database
import init


@csrf_exempt
def index(request):
    init.first()
    
    u = ''
    v = ''
    if request.POST.has_key('pretask'):
        u = str(request.POST['pretask'])
        v = str(request.POST['subtask'])

    else:
        return render_to_response('prepage.html')
    
    try:
        database.execute('insert edges (u,v) values(\'%s\',\'%s\')' % (u,v))
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        fw = open('error.txt','w')
        fw.write("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        fw.close()
    return render_to_response('prepage.html', {'loadvalue': 'yes'})
    
