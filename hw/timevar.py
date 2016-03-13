import os
import sys
import re
import time

def timevar(code):
    now = time.ctime()
    now = now.replace(' ','_')
    code = code.replace('${now}', now)
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    code = code.replace('${today}', today)
    return code