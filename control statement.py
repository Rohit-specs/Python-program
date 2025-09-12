list=[]

list.append(int(input("Enter number 1: ")))
list.append(int(input("Enter number 2: ")))
list.append(int(input("Enter number 3: ")))
list.append(int(input("Enter number 4: ")))
list.append(int(input("Enter number 5: ")))

# list.append(list[0])
# list.append(list[1])
# list.append(list[2])
# list.append(list[3])
# list.append(list[4])

print(list)
positivenumber=0
negetivenumber=0
zero=0
if list[0]>0:
    positivenumber+=1
elif list[0]==0:
    zero+=1
else:                             
    negetivenumber+=1
if list[1]>0:
    positivenumber+=1
elif list[1]==0:
    zero+=1
else:
    negetivenumber+=1
if list[2]>0:
    positivenumber+=1
elif list[2]==0:
    zero+=1
else:
    negetivenumber+=1
if list[3]>0:
    positivenumber+=1
elif list[3]==0:
    zero+=1
else:
    negetivenumber+=1
if list[4]>0:
    positivenumber+=1
elif list[4]==0:
    zero+=1
else:
    negetivenumber+=1
print("Positive number: ",positivenumber)
print("Negetive number: ",negetivenumber)
print("Zero's         : ",zero)








