# Create a program to create a following form inputs as CLI inputs 
import json
from json.decoder import JSONDecodeError
import os


while True:
    dic={}
    name = input("Enter your name: ")
    DOB = input ("Enter your birthdate in dd/mm/yy: ")
    age = int(input("Enter your age: "))
    hobby = list(map(str, input("Enter your hobby: ").strip().split(',')))

    dic['Name']=name
    dic['DOB']=DOB
    dic['Age']=age
    dic['Hobby']=hobby

    # conversion to JSON done by dumps() function and serializing the python object
    with open("data.json", 'r+') as infile, open("data.json", 'w') as outfile:
        try:
            # First we load existing data into a dict.
            if os.path.getsize('data.json') > 0:
                # First we load existing data into a dict.
                file_data = json.load(infile)
                # Join new_data with file_data inside emp_details
                file_data.append(dic)
                # Sets file's current position at offset.
                infile.seek(0)
                # convert back to json.
                json.dump(file_data, infile, indent = 4)
            else:
                json.dump(dic, outfile)
        except JSONDecodeError:
            pass

    add_seg = input("Do you want to enter details again(y/n):")
    if (add_seg == 'Y')|(add_seg == 'y'):
        continue
    else:
        break
    
with open("data.json", "r") as read_it:
    data = json.load(read_it)
    print(data)
