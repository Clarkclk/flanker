from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import sys
import init

@csrf_exempt
def store(request):
    init.first()
    
    ans = "storevalue"
    codename = str(request.POST.get('codename', ""))
    if(codename != ""):
        fr = open('store.sql', 'r')
        texts = fr.read()
        fw = open(codename, 'w')
        fw.write(texts)
        ans = "yes"
        fr.close()
        fw.close()

    return render_to_response('storepage.html', {'storevalue': ans})
