from datetime import datetime
"""
This program will print out the basic information of the author 

@name programmer's name
@labNum  lab number
@labName lab's name
"""
def print_first(name,labNum,labName):

# name = "CNET-142: Ziwen li"
# labName = "Lab 4: Functions"
    time = datetime.now()
    currenTime = time.strftime("%Y-%m-%d %H:%M:%S")

    msg = "CNET-142 : "+name + '\n'
    msg = msg+ "Lab"+ "{:6}".format(labNum) +": "+ labName+"\n"
    msg = msg +"{:9}".format("Time") +": " +currenTime + "\n"
    return(msg)
