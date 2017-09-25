### IMPORTO
import time
import datetime
#import pandas #timedelta to int function test
#from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

### INPUT FROM THE CMD ###
fmt = '%H:%M'
timeobject = raw_input("Insert time you arrived in HH:MM format : \n")
start = datetime.datetime.strptime(timeobject,fmt)
now = datetime.datetime.now()


### DateTime Variables ###
first = start + datetime.timedelta(minutes=360)
second = start + datetime.timedelta(minutes=510)
last = start + datetime.timedelta(minutes=645)
elapsed = now - start

### OUTPUT ###
print ("You can leave @ " + str(datetime.datetime.strftime(first,fmt)) + " without a Pause\n" )
print ("You can leave @ " + str(datetime.datetime.strftime(second, fmt)) + " with a 30 Minutes Pause\n" )
print ("You have 2 leave @ " + str(datetime.datetime.strftime(last,fmt)) + " with a 30 and a 15 Minutes Pause\n" )
print ("Time elapsed since work started: " + str(elapsed.seconds/3600) +":"+ str((elapsed.seconds%3600)/60))

### Output on breaks ###
if(elapsed.seconds) <= 6*3600 :
    print "You have to go on a break in: " + str((6*3600 - elapsed.seconds)/60) + " minutes\n"
elif(elapsed) > (6*3600) and (elapsed) <=(9*3600):
    print "You already had a 30 minutes Break \n"
else:
    print "You are working on the limit and getting another 15 Minutes of break \n"

### Percentage of the Day ###
prozent = 3600/10
percent= elapsed.seconds/prozent

### CMD OUTPUT Percentage ###
print "You are at " + str(percent) +  "%. Hang in there!\n"
print "[" + percent*"#" + (100-percent)*"." +  "]"
