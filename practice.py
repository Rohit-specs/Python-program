
# studentdetails=[]
# studentdetail={}
# studentqualification=[]
# studentdetail["firstname"]="rohit"
# studentdetail["lastname"]="kumar"
# studentdetail["age"]=18
# studentdetail["contact"]=1234567890
# studentdetail["address"]="Bageshwar"
# studentdetail["qualification"]=studentqualification
# user1={}
# user1["qualificationname"]=input("Enter your qualification name: ")
# user1["qualificationyear"]=int(input("Enter your qualification year: "))
# studentqualification.append(user1)
# studentdetails.append(studentdetail)
# print(studentdetails)

studentdetails=[]
qualifications=[]
user1={}
user1["name"]="Rohit"
user1["age"]=18
qualifications=[{"qualificationname":input("Enter your qualification: "),
                "qualificationyear":int(input("Enter your qualification year: "))},
                {"qualificationname":input("Enter your qualification: "),
                "qualificationyear":int(input("Enter your qualification year: "))}]
user1["studentqualifications"]=qualifications

studentdetails.append(user1)
print(studentdetails)
