from ..secondpackage import studentdetail

def menu():
    print("1. Enter Student detail")
    print("2. View student detail")
    print("3. Update student record")
    print("4. Exit")
    choice=int(input("Please enter a choice: "))
    if choice==1:
        studentdetail.studentrecord()
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    else :
        print(choice +"is not a valid option! ")
    