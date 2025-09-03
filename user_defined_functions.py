students = []  

def menu():
    print("\n--- Student Management ---")
    print("1. Register student")
    print("2. View all student records")
    print("3. View record by student ID")
    print("4. Delete record by student ID")
    print("5. Exit")
    option = input("Please enter a choice: ")
    return int(option)

def registerstudent():
    user = {}
    user["id"] = int(input("Please enter your id: "))    
    user["name"] = input("Please enter your name: ")    
    user["address"] = input("Please enter your address: ")
    students.append(user)
    print("Student registered successfully!")

def students_records():
    if not students:
        print("No student records available")
    else:
        print("All Student Records:")
        for i in students:
            print(i)

def view_student_record():
    searchvalue = int(input("Please enter student id: "))
    found = False
    for i in students:
        if i["id"] == searchvalue:
            print("Student found:", i)
            found = True
            break
    if not found:
        print("No student found with that ID.")

def delete_record():
    searchvalue = int(input("Enter ID to delete: "))
    for i in students:
        if i["id"] == searchvalue:
            students.remove(i)
            print("Record deleted successfully.")

while True:
    output = menu()
    if output == 1:
        registerstudent()
    elif output == 2:
        students_records()
    elif output == 3:
        view_student_record()
    elif output == 4:
        delete_record()
    elif output == 5:
        print("Exit successfully")
        break
    else:
        print("Invalid choice!, try again")
