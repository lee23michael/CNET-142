from datetime import datetime
import sys
import os
"""
This program will print out author's name, program name, and currnt time
@name programmer's name

"""
def print_first(name):

# name = "CNET-142: Ziwen li"
# labName = "Lab 4: Functions"
    time = datetime.now()
    currenTime = time.strftime("%Y-%m-%d %H:%M:%S")

    fileName = os.path.basename(sys.argv[0])

    msg = "Name\t\t: "+name + '\nprogram\t\t: '+fileName+\
    "\nCurrent Time\t: " + str(currenTime)[:19]
 
    return(msg)
