import sys
import os
import database
import time
import newtask
import subprocess
import string
from apscheduler.schedulers.blocking import BlockingScheduler


def first():
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if(os.path.exists('date.log')):
        fr = open('date.log', 'r')
        s = fr.read()
        fr.close()
        
        if(s != today):
            init()
            return True
    else:
        init()
        return True
    
    return False

def checktask(task):
    res = str(database.getlist('select type from tasklist where name = \'%s\'' %task)[0])
    if(newtask.judge(task)):
        if(res == 'None'):
            subprocess.Popen('python hw/scheduler.py %s %s.sql' %(task,task), shell = True)
        else:
            timelist = res.split('-')
            hour = timelist[0]
            minute = timelist[1]
            subprocess.Popen('python hw/timetask.py %s %s %s' %(task,hour,minute), shell = True)
            

def init():    
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    database.init()
    database.execute('update tasklist set status = \'started\'')
    fw = open('date.log', 'w')
    fw.write(today)
    fw.close()
    tasklist = database.getlist('select name from tasklist')
    statuslist = database.getlist('select status from tasklist')
    for i in range(0,len(tasklist)):
        if(statuslist[i] == 'started'):
            checktask(tasklist[i])