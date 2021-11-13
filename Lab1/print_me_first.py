from datetime import datetime

NAME = "CNET-142 Ziwen Li"
labname = "Lab1-Print Name"
currenttime = datetime.now()
timestamp = currenttime.strftime("%b-%d-%Y %a (%H:%M:%S)")
print ("{:10}".format("Name"),":",NAME)
print ("{:10}".format("Lab"),":",labname)
print ("Currentime :",timestamp)

