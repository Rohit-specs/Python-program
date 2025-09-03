import json
studentdata={}
studentdata["student id"]=input("Please Enter Your student id: ")
studentdata["name"]=input("Please Enter Your Name: ")
studentdata["age"]=int(input("Please Enter Your age: "))
studentdata["contact"]=int(input("Please Enter Your contact: "))
studentdata["email"]=input("Please Enter Your email id: ")
studentdata["educational_Qualification"]=input("Please Enter Your educational qualification: ")
studentdata["nationality"]=input("Please Enter Your Nationality: ")
studentdata["gender"]=input("Please Enter Your Gender: ")
studentdata["date_of_birth"]=input("Please Enter Your Date of birth: ")
studentdata["guardian"]=input("Please Enter Your Guardian Name: ")
studentdata["gpa"]=float(input("Please Enter Your College GPA: "))
studentdata["attendence"]=float(input("Please Enter Your Attendence Percentage: "))
studentdata["language_spoken"]=input("Please Enter your spoken language: ")
studentdata["date_enrollment"]=input("Please Enter Your Date of enrollment: ")
del studentdata["name"]
del studentdata["sutudent id"]
countrycapital={
    
    "india": {"id": 1, "capital": "delhi"},
    "usa": {"id": 2, "capital": "washington"},
    "nepal": {"id": 3, "capital": "kathmandu"},
    "korea": {"id": 4, "capital": "seoul"},
    "china": {"id": 5, "capital": "beijing"},
    "pakistan": {"id": 6, "capital": "islamabad"},
    "srilanka": {"id": 7, "capital": "colombo"},
    "bhutan": {"id": 8, "capital": "thimphu"},
    "france": {"id": 9, "capital": "paris"},
    "united kingdom": {"id": 10, "capital": "london"},
    "afganistan": {"id": 11, "capital": "kabul"},
    "chile": {"id": 12, "capital": "santiago"},
    "cuba": {"id": 13, "capital": "havana"},
    "egypt": {"id": 14, "capital": "cairo"},
    "japan": {"id": 15, "capital": "tokyo"},
    "russia": {"id": 16, "capital": "moscow"},
    "brazil": {"id": 17, "capital": "brasilia"},
    "canada": {"id": 18, "capital": "ottawa"},
    "germany": {"id": 19, "capital": "berlin"},
    "newzealand": {"id": 20, "capital": "wellington"}
    
    }
print(json.dumps(countrycapital, indent=20))

countrycapital["india"] = "delhi"
countrycapital["usa"] = "wasington"
countrycapital["nepal"] = "katmandu"
countrycapital["korea"] = "soeul"
countrycapital["china"] = "beiging"
countrycapital["pakistan"] = "islamabad"
countrycapital["srilanka"] = "colombo"
countrycapital["bhutan"] = "thimpu"
countrycapital["france"] = "paris"
countrycapital["united kingdom"] = "london"
print(json.dumps(countrycapital,indent=10))



