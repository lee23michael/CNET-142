# This funcion wil open the file fileName and counts how many lines, words and chars 
# in the file, and place each line of the file in the lineList parameter.   
# The function returns numOfLine, numOfWords, numOfChars as return value,  
# and lineList as parameter  
#  
#   numOfLine:  number of lines in the file 
#   numOfWords:  number of lines in the file 
#   numOfChars:  number of lines in the file 
# @parm:  fileName - this is the filename to be opened 
# @parm:  lineList - this list contains all the text in each of lines 
#                   from the file. Each line of text is added to the list. 
#                   Need to remove the new line feed '\n' from the line 
#                   before adding to the list.  
# @return numOfLine, numOfWords, numOfChars 

def count(fileName,lineList):
  #fileName = input("Input file name: ")
    numOfLine = 0  
    numOfChars = 0 
    numOfWords = 0  
    try :
        infile = open(fileName,'r')
    except IOError: 
        print("Error : cant open file ", fileName)
    else:
        lines = infile.readlines() # read flie by lines and put into a list "line"
        for i in range(len(lines)):
            lines[i]= lines[i].rstrip('\n') # delete the line feed
            lineList.append(lines[i])       # add each line to lineList

        # The length of lineList is the number of lines
        numOfLine = len(lineList)           
        infile.close()

    try :
        infile = open(fileName,'r')
    
        content = infile.read()     # read entire file
        numOfChars = len(content)   # length of the file will be the number 
                                    # the number of characters 

        words = content.split()     # store words in to list "words"
        numOfWords = len(words)     # lenght of list is the number of words        
       #line = infile.readline()
      #  line = content.split('\n')
      #  numOfLine = len(line)
      # print(lineList)
        
  #      while line != '':
  #          numOfLine +=1   
  #          line = line.rstrip('\n')      
  #          lineList.append(line)  
  #          line = infile.readline()
    except IOError: 
        print("Error : cant open file ", fileName)
        infile.close()
        
    return numOfLine,numOfWords,numOfChars  


    