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
def load(request):
    init.first()
    
    codeList = []
    #for filename in glob.glob(r'
    path = os.path.dirname(os.path.abspath("store.sql"))
    #codeList.append(path)
    fileList = os.listdir(path)
    for oneFile in fileList:
        m = re.match("^\w+.sql$", oneFile)
        if(m != None):
            codeList.append(oneFile)
            
    strs = 'r\'' + path + '\\*.sql'
    for fileName in glob.glob(strs):
        codeList.append(filename)
    
    loadvalue = 'no'
    if request.POST.has_key('codelist'):
        sqlName = ''
        sqlName = str(request.POST['codelist'])
        fr = open(sqlName, 'r')
        code = fr.read()
        fr.close()
        fw = open("load.sql", 'w')
        fw.write(code)
        fw.close()
        loadvalue = 'yes'
        
    return render_to_response('loadpage.html', {'codelist':codeList, 'loadvalue':loadvalue})
