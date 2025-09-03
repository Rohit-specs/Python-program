list=[]

user1={"id":int(input("Enter your id: ")),
         "name":input("please enter your name: "),
         "address":input("Please enter your address: "),
         "qualification":{
                            "qualification1":input("Enter your qualification: "),
                            "qualification1_passing_year":int(input("Enter your class 10 passing year: ")),
                            "qualification2":input("Enter your qualification: "),
                            "qualification2_passing_year":int(input("Enter your class 12 passing year: ")),
                            "latest_qualification":(input("Enter your latest qualification: ")),
                            "latest_qualification_year":int(input("Please enter your latest qualification year: "))
                         }
}
         

list.append(user1)
print(user1.get("qualification"))

user2={"id":int(input("Enter your id: ")),
         "name":input("please enter your name: "),
         "address":input("Please enter your address: "),
         "qualification":{
                            "qualification1":input("Enter your qualification: "),
                            "qualification1_passing_year":int(input("Enter your class 10 passing year: ")),
                            "qualification2":input("Enter your qualification: "),
                            "qualification2_passing_year":int(input("Enter your class 12 passing year: ")),
                            "latest_qualification":(input("Enter your latest qualification: ")),
                            "latest_qualification_year":int(input("Please enter your latest qualification year: "))
                         }
}
         

list.append(user2)
print(user2.get("qualification"))





# print(list)
