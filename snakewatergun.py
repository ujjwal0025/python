import random
print ("enter S for snake and W for water and G for gun...")
a=input()
b=("snake","water","gun")
c=random.choice(b)
#
if (a=='s' and c=="water"):
    print("you won")
elif (a=='s' and c=="gun"):
    print("you lose !! ")
elif (a=='w' and c=="gun"):
    print("you won!!")
elif (a=='w' and c=="snake"):
    print("you lose!!")
elif (a=='g' and c=="snake"):
    print("you won!!")
elif (a=='g' and c=="water"):
    print("you lose!!")
else:
    print("tie both are equal!!")
print("computer chices =",c)