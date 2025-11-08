import json
import os
import datetime

def valid_id():
    while True:
        try:
            id=int(input("Enter your student ID: "))
            return id
        except Exception as e:
            print(e)
            
def valid_name():
    while True:
        try:
            name=input("Enter your name: ")
            return name
        except Exception as e:
            print(e)
            
            
def valid_email():
    while True:
        try:
            email=input("Enter your email id: ")
            return email
        except Exception as e:
            print(e)

path="database\\data.json"
studentdata=[]

def studentregistration():
    print("-----------Student Registration-----------")
    with open(path,'r') as file:
        dataoutput=json.loads(file.read())
        studentdata=dataoutput 
    user={}
    # id=input("Enter your student ID: ")
    user["id"]=valid_id()
    user["name"]=valid_name()
    user["address"]=input("Enter your address: ")
    user["email"]=input("Enter your email id: ")
    qualification=[]
    while True:
        qualificationdetails={}
        qualificationdetails["qname"]=input("Please enter your qualification name: ")
        qualificationdetails["qyear"]=input("Please enter your qualification year: ")
        qualification.append(qualificationdetails)
        choice=input("Do you want to add more qualification details (yes/no): ")
        if choice.lower()!="yes":
            break        
    user["qualifications"]=qualification
    user["registration_date&time"]=str(datetime.datetime.now())
    studentdata.append(user)
    with open(path,'w') as file:
        file.write(json.dumps(studentdata, indent=2))
    print("Student registration completed!")
