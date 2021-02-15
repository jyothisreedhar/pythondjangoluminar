#from random import *
#from os import *
f=open("userlist","r")
lst=[]
for lines in f:
    name,score=lines.rstrip("\n").split(",")
    print(lst.add(lines))
