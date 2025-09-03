userdetail = {
    "email": "rohit@gmail.com", 
    "password": "123456789"
}

while True:
    print("\n==== Main Menu ====")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        while True:
            email = input("Please enter registered email: ")
            if email != userdetail["email"]:
                print("Incorrect email! Please try again.")
                continue

            password = input("Enter password: ")
            if password != userdetail["password"]:
                print("Incorrect password! Please try again.")
                continue

            print("Login successful!\n")

            while True:
                print("\n--- User Dashboard ---")
                print("1. View user details")
                print("2. Update user details")
                print("3. Logout")

                choice1 = int(input("Enter your choice: "))

                if choice1 == 1:
                    print("\nUser Details:")
                    for key, value in userdetail.items():
                        print(f"{key.capitalize()}: {value}")

                elif choice1 == 2:
                    choice2 = input("What would you like to update (email/password/both): ").lower()

                    if choice2 == "email":
                        userdetail["email"] = input("Enter new email: ")

                    elif choice2 == "password":
                        userdetail["password"] = input("Enter new password: ")

                    elif choice2 == "both":
                        userdetail["email"] = input("Enter new email: ")
                        userdetail["password"] = input("Enter new password: ")

                    else:
                        print(f"'{choice2}' is not a valid option!")

                elif choice1 == 3:
                    print("Logged out successfully.")
                    break

                else:
                    print(f"{choice1} is not a valid option!")

            break  

    elif choice == 2:
        print("\n--- Signup ---")
        userdetail = {}
        userdetail["name"] = input("Please enter your name: ")
        userdetail["contact"] = int(input("Please enter your phone number: "))
        userdetail["email"] = input("Please enter your email: ")
        userdetail["password"] = input("Please enter your password: ")

        print("Signup completed successfully!")

    elif choice == 3:
        print("Exiting... Goodbye!")
        break

    else:
        print(f"{choice} is not a valid option!")
