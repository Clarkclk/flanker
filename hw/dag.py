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

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        
@csrf_exempt        
def index(request):
    init.first();
    
    tasklist = database.getlist('select name from tasklist')
    u = database.getlist('select u from edges')
    v = database.getlist('select v from edges')
    
    edges = []
    for i in range(0,len(u)):
        edges.append(Edge(u[i], v[i])) 
    
    fw = open('debug_dag', 'w')
    for j in edges:
        fw.write(j.u)
    fw.close()
    
    return render_to_response('chart2.html', {'tasklist': tasklist,'edgelist': edges})
