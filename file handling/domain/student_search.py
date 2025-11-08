import json
import os
path="database\\data.json"
def studentsearch():
    print("-------Search Student-------")
    searchby=input("Enter your search by (name/email/id): ")
    searchby=searchby.lower()
    
    with open(path,'r') as file:
        data=file.read()
        data=json.loads(data)
        if searchby=="name" or searchby=="email" or searchby=="id":
            searchvalue=input(f"Please enter your {searchby}: ")
            for i in data:
                if i[searchby]==searchvalue:
                    i=json.dumps(i,indent=2)
                    print(i)
        elif searchby == "qualification":
            qname = input("Please enter your qualification name: ")
            qyear = input("Please enter your qualification year: ")
            for i in data:
                for q in i.get("qualifications"):
                    if q.get("qname") == qname and q.get("qyear") == qyear:
                        print(json.dumps(i, indent=2))
                        break             
        else:  
            print(f"{searchby} is not a valid input!")
                



        
        
    
             
