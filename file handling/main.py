import json
# from domain.student_registration import studentregistration
# from domain.menu import mainmenu
# from domain.student_search import studentsearch
# from domain.all_studentrecord import allstudentrecord
from domain import *

while True:
    options=int(mainmenu())
    if options==1:
        studentregistration()
        options=None
    elif options==2:
        studentsearch()
    elif options==3:
        allstudentrecord()
    elif options==4:
        print("Thank you for visiting.")
        break
    else:
        print(options,"is not a valid choice")
        print("Please try again.")
