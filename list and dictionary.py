list=[]
for i in range (2):
    dictionary={}
    dictionary[id]=int(input("Enter student id: "))
    dictionary["name"]=input("Enter student name: ")
    dictionary["address"]=input("Enter student address: ")
    list.append(dictionary)
searchby=input("Search by (id/name/address): ")
if searchby=="id"or searchby=="name" or searchby=="address":
    searchvalue=input(f"Enter {searchby}: ")
else:
    print(f"{searchby} is not valid!")
for i in list:
    if dictionary[searchby]==searchvalue:
        user=dictionary
        found=True
        break
print(user)