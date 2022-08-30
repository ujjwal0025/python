import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrtsuvwxyz"
num="0123456789"
symbol="@#$%^&()*_-?{}[]"
gen=upper+lower+num+symbol
length=8
password="".join(random.sample(gen,length))
print("gentrated password is : ",password)