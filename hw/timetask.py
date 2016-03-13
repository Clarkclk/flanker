from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import newtask
import string


task = str(sys.argv[1])
hour = str(sys.argv[2])
minute = str(sys.argv[3])
print task
print hour
print minute
scheduler = BlockingScheduler()
tmp = {'taskname':task,'sqlfile':'%s.sql' %task}
scheduler.add_job(newtask.runsql(**tmp), 'cron', hour = string.atoi(hour), minute = string.atoi(minute))
scheduler.start()