import random
def check(computer, user):
    if(computer == user):
        print("DRAW!")
        return 0
    if(computer == 0 and user == 1):
        return -1
    if(computer == 2 and user == 0):
        return -1
    if(computer == 1 and user == 2):
        return -1
    return 1
print("** <- ___________ENTER NUMBERS -> !! 0 -> SNAKE 1 ->WATER  AND 2 -> GUN ____________________ -> **")


user= int(input("ENTER (0,1,2 ) FOR PLAY (YOUR INPUT):  "))
if(user > 2):
    print("!!!!! ERROR 404( INVALID INPUT !!!!! )")
computer = random.randint(0,2)
score =check(computer, user)
print("YOUR INPUT: ", user)
print("COMPUTER'S INPUT: ", computer)
if(computer==user):
    print("!!!!! IT'S DRAW !!!!!")
elif(score == -1):
    print("!!!!! YOU LOST !!!!!")
else:
    print("!!!!! YOU WON !!!!!")