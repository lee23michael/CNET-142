import printFirst
import json
"""
"""


"""
create_my_contact() will return a dictionary which contains the data used in
this program
"""
def create_my_contact():
    myContact = {"01": { "firstName" : "John", 
                        "lastName" : "Smith" ,
                        "DOB" : "1/20/1991" ,
                        "phoneNum" : {"number" :  "510-600-5400", 
                                      "type" :  "cell" },
                        "address" : {"street" :  "100 main street" ,
                                      "city" :  "Fremont", 
                                      "state" :  "CA" ,
                                      "zipcode" :  "94536" }
                        },# 01 keypair
                 "02" :  { "firstName" : "Ron", 
                           "lastName" : "Robertson",
                           "DOB" : "5/23/1991", 
                           "phoneNum" : {"number" : "510-600-8800", 
                                         "type" : "cell" },
                           "address" : {"street" :  "4600 Ohlone Way", 
                                      "city" :  "Fremont", 
                                      "state" :  "CA", 
                                      "zipcode" : "94539" }
                        },# 02 keypair
                "03" : {"firstName" : "Paul", 
                        "lastName" : "Washington", 
                        "DOB" :  "6/15/1995", 
                        "phoneNum" : {"number" : "510-688-1241" , 
                                       "type" : "cell"} ,
                        "address" : {"street" : "8543 Ohlone Plaza", 
                                  "city" : "Fremont", 
                                  "state" : "CA", 
                                  "zipcode" : "94539" },
                        }# 03 keypair
                } # myContact ends
    return myContact


"""
save_json_file() will save a dictionary to JSON file format

@fileName: the name of a JSON file that will be saved to
@content: the dictionary 

"""
def save_json_file(fileName,content):
    json_file = json.dumps(content,indent = 3)
    with open(fileName,'w') as outfile:
        outfile.write(json_file)
    outfile.close()
    


"""
open_json_file() will open a JSON file and load to a dictionary

@fileName: name of the JSON file

"""
def open_json_file(fileName):
    with open(fileName,'r') as json_file:
        info = json.load(json_file)
        return info
    
"""
find_my_contact_key() will find whether a content is in a dictionary
if the content found, it will print out the crossponding information
such as name,birthday,phone number, and address

@searchKey: the content will be searched
@my_contact: the dictionary loaded from a JSON file

"""
def find_my_contact_key(searchKey,my_contact):
        found = False
        print("*** Search for ",searchKey)
        for key,value in my_contact.items():
                
            if (value == searchKey):
                print("***",searchKey,"found***")
                print("Key: ", key)
                print("Value: ",value)
                found = True
            else:
                for key1,value1 in value.items():
                    if (value1 == searchKey):
                        print("***",searchKey,"found***")
                        print("Name:","{:>8}".format(value["firstName"]),
                        value["lastName"])
                        print("Birthday: ", value["DOB"])
                        print("{:>4}:".format(value["phoneNum"]["type"]),
                        "{:>17}".format(value["phoneNum"]["number"]))
                        print("Address:","{:>17}".format(value["address"]["street"]),'\n',
                        "{:>17},".format(value["address"]["city"]),value["address"]["state"],
                        value["address"]["zipcode"])
                        found = True
        if not found:
                print("***",searchKey,"not found***")
                        
        return found





def main():
    printMe = printFirst.print_first("Ziwen Li",6,"Dictionary")
    print(printMe) 
    contact_list = create_my_contact() # create dictionary 
    save_json_file("my_contact.json", contact_list) # save disctionary to JSON file 
 
    json_data = open_json_file('my_contact.json') #open JSON file load to distionary 
    print("***BEGINNING OF JSON List: \n", contact_list,  
          "\n***END OF JSON LIST\n\n") 
         
    find_my_contact_key("Ron", json_data) # find record 'Ron' 
    find_my_contact_key("Sha", json_data) # find record 'Sha' 


if __name__ == '__main__': 
    main()