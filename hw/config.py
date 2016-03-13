#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import sys
import glob
import os
import re
import init


@csrf_exempt
def config(request):
    
    init.first()
    
    status = 'no'
    
    if request.POST.has_key('sqladdress'):
        address = str(request.POST['sqladdress'])
        sql = str(request.POST['sqlsql'])
        name = str(request.POST['sqlname'])
        password = str(request.POST['sqlpassword'])
        
        if address != '' and sql != '' and name != '' and password != '':
            status = 'yes'
            fw = open("config.txt", "w")
            fw.write(address+'\n')
            fw.write(sql+'\n')
            fw.write(name+'\n')
            fw.write(password+'\n')
            fw.close()
    
    return render_to_response('configpage.html',{'configvalue':status})
