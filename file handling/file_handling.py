import datetime
list=[]
def function():
    id=None
    name=None
    email=None
    time=None
    id=input("enter your id: ")
    name=input("enter your name: ")
    email=input("enter your email id: ")
    time=datetime.datetime.now()
    return id,name,email,time
path="C:\\Users\\lenovo\Desktop\\-Restaurant-Where-Food-Meets-Creativity-\\Python\\Python github reopsitory July2025 batch\\folder"
n=int(input("No. of file you want to create? : "))
for i in range(n):
    id=None
    name=None
    email=None
    time=None
    id=input("enter your id: ")
    name=input("enter your name: ")
    email=input("enter your email id: ")
    time=datetime.datetime.now()
    data=(f"ID={id}\nName={name}\nEmail id={email}\nCurrent Time={time}")
    with open(f"{path}\\sample{i+1}.txt",'w') as file:
        file.write(data)
        print("\n")
    with open(f"{path}{i+1}",'r') as file:
        print(file.read())
# choice=input("\npress append for appending data\n otherwise press any key :")
# if choice=="append":
#     filename=input("enter file name with extention: ")
#     with open(f"{path}{filename}]",'a') as file:
#         append=input("you want to append something : ")
#         file.write(f"{append}")
#         print("do you want to see the changes you make in the file\nfor that enter showfile: ")
#         option=input()
#         if option=="showfile":
#             with open(f"{path}{filename}]",'r') as file:
#                 print(file.read())