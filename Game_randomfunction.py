import random
def points(count,counter):
    print(f"\nyour point {10-counter}")
    print(f"computer points {10-count} \n")
count=10
counter=10
list=["stone","paper","scissor"]
while (True):
    computer=random.choice(list)
    user=input("Choose stone,paper,scissor: ")
    user=user.lower()
    if user in list and count>=0 and counter>=0:
        if computer==user:
            print("--------draw--------")
            print(f"you and computer both selected {computer}\n")
        elif computer=="stone": 
            if user=="paper":
                print("Player won round")
                count-=1
                points(count,counter)
            elif user=="scissor":
                print("computer won round")
                counter-=1
                points(count,counter)
        elif computer=="paper" :
            if user=="stone":
                count-=1
                print("computer won round")
                points(count,counter)
            elif user=="scissor":
                counter-=1
                print("Player won round")
                points(count,counter)
        elif computer=="scissor":
            if user=="paper":
                count-=1
                print("computer won round")
                points(count,counter)
            elif user=="stone":
                print("Player won round")
                counter-=1
                points(count,counter)
    elif counter==0:
        print("computer won the game")
        points(count,counter)
    elif count==0:
        print("player won the game")                
        points(count,counter)
    else:
        print(f"{user} is not in {list}")