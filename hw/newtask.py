import subprocess
import MySQLdb
import sys
import os
import database
import thread

def runsql(taskname,sqlfile):
    
    username = 'root'
    password = 'flanker'
    if(os.path.exists('config.txt')):
        fr = open("config.txt","r")
        list_of_all_the_lines = fr.readlines()
        username = list_of_all_the_lines[2][0:-1]
        password = list_of_all_the_lines[3][0:-1]
        fr.close()
    
    cmd = "mysql -h localhost -u %s -p%s < %s" %(username, password, sqlfile)
    ferr = open('test.txt','w')
    ferr.write('update tasklist set status = \'running\' where name = \'%s\'' %taskname)
    ferr.close()
    database.execute('update tasklist set status = \'running\' where name = \'%s\'' %taskname)
    child = subprocess.Popen(cmd, shell = True)
    child.wait()
    
    database.execute('update tasklist set status = \'finished\' where name = \'%s\'' %taskname)
    
    nexttask = database.getlist("select name from tasklist where status = \'started\'")
    for task in nexttask:
        
        #parent = database.getlist("select u from edges where v = \'%s\'" %task)
        #if taskname not in parent:
            #continue
        
        if judge(task):
            thread.start_new_thread(runsql, (task, '%s.sql' %task)) 
 
def judge(task):
    parent = database.getlist("select u from edges where v = \'%s\'" %task)
    
    for i in parent:
        result = database.getlist("select name from tasklist where name = \'%s\' and status = 'finished'" %i)
        if len(result) == 0:
            return False
    return True