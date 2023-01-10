#Digital Version of Hand Cricket
#Developed by Madhav Kumar

#required components

import random
mknc=0 #ye bas ek helping variable hai jo help from nowhere karta hai

#entering the match

print("Welcome the Match.")
print("How much matches do you wan't to play?")
m=int(input()) #no. of matches
print("How much balls do you want to play?")
b=int(input()) #no. of balls
print("You will bat first")
rp=int() #runs of player
rc=int() #runs of computer
print("Start Batting")

for j in range(m):
    for i in range(b):
        mknc+=1

#play field

        p=int(input()) #player
        c=int(random.choice(range(1,7))) #computer
        print(c)

#main algorithm

        if p!=c and p in range(7):
            rp+=p
            if mknc<b:
                print("Next ball")
            else:
                print("Your batting is done")
                print("Your total runs are ",rp)
                print("Now it's my batting")
        elif p==c:
            print("You're Out!")
            print("Your total runs are ",rp)
            print("Now it's my batting")
            break
        else:
            print("You Missed the ball!")

#batting of the computer
            
    mknc=0
    for k in range(b):
        mknc+=1

#play field

        p=int(input()) #player
        c=int(random.choice(range(1,7))) #computer
        print(c)

#main algorithm

        if rc>rp:
            break
        elif p!=c:
            rc+=c
            if mknc<b:
                print("Next ball")
            else:
                print("Game Over")
        elif p==c:
            print("I am Out!")
            print("Game Over")
            break

    print("My total runs are ",rc)
    print("And Your total runs are ",rp)
    break

#final conclusion of the match

if rc<rp:
    print("You Won")
elif rp<rc:
    print("You Lost")
else:
    print("Draw Match!")

#I AM DONE
