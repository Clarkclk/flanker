#!/usr/bin/env python

import sys
import newtask

#print sys.argv
#print sys.argv[1]
#print sys.argv[2]
newtask.runsql(str(sys.argv[1]),str(sys.argv[2]))

#fw = open('testsch.txt','w')
#fw.write(str(sys.argv[1]))
#fw.close()
