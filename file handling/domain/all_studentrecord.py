import json
import os
def allstudentrecord():
    print("----------All Student Details----------")
    with open("database\\data.json",'r') as file:
        data=file.read()
        print(data)
        