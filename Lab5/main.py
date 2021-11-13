import printFirst
import count
import others

def main():

    info = printFirst.print_first("Ziwen Li",5,"FileCounter")
   
    print(info)  

    fileList = []
    
    inputFileName = input("Input file name: ")
    #inputFileName = "test.txt"
    
    
    content = count.count(inputFileName,fileList)
    other = others.others(inputFileName)

    for i in range(len(fileList)):
        print("Line",i,":",fileList[i])

    msg = "Total number of Lines : " + str(content[0])+"\n"
    msg = msg + "Total number of Words : " + str(content[1]) +'\n'
    msg = msg + "Total number of Characters : " + str(content[2]) +'\n'
    msg = msg + "Total number of Upper letters : " + str(other[0]) +'\n'
    msg = msg + "Total number of Lower letters : " + str(other[1]) +'\n'
    msg = msg + "Total number of Space : " + str(other[2]) +'\n'
    msg = msg + "Total number of Didgits : " + str(other[3]) +'\n'
    msg = msg + "Total number of Sentences : " + str(other[4]) +'\n'



    print(msg)

        



if __name__ == "__main__":
    main()