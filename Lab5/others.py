# This funcion wil open the file fileName and counts how many lppercase letters, lowercase letters, spaces, digits, 
# sentences. a
# The function must RETURN numOfLine, numOfWords, numOfChars as return value,  
# and lineList as parameter  
#  
#   upper:  number of upper case letter in the file 
#   lower:  number of lower case letter  in the file 
#   digit:  number of digits in the file 
#   sentence: number of sentences in the file
# @parm:  fileName - this is the filename to be opened 
# @return upper,lower,space, digit,sentence


from io import UnsupportedOperation


def others(fileName):
 
    try :
        infile = open(fileName,'r')
        upper = 0
        lower = 0
        digit = 0
        sentence = 0
    
        content = infile.read()

        space = content.count(" ")
       # se = content.count("!") + content.count("?")+content.count(".")
        
        for i in content:
          if i.isupper():
              upper +=1
          elif i.islower():
              lower +=1 
          elif i.isdigit():
              digit +=1
          elif i == "." or i == "?" or i == "!":
              sentence += 1



       # print(upper,lower,space, digit,sentence)
      
    except IOError: 
        print("Error : cant open file ", fileName)
        infile.close()

    return(upper,lower,space, digit,sentence)
