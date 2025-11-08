from package import *
# from package import division
# from package import multiplication
# from package import subtraction





a=float(input("Please enter number1: "))
operator=input("Enter operator for calculation (+,-,/,*): ")
b=float(input("Please enter number2: "))
if operator == "+":
    print(addition(a,b))      
elif operator =="-":
    print(subtraction(a,b))
elif operator =="*":
    print(multiplication(a,b))
elif operator =="/":
    print(division(a,b))  
else:
    print(operator +"is not correct option!")    