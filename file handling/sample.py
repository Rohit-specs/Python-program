
n=int(input("No. of file you want to create? "))
for i in range (n):
    filename="sample"
    with open(f"newfolder\\{filename}{i}.txt",'w') as file:
        # data=input(f"what you would like write in file no{i+1}: ")
        # file.write(data)
        pass                  
    