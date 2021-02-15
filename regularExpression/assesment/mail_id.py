f1= open("mailid", "r")
f2= open("mailid", "w")
from re import *

# phone_num=int(input("enter the phone number:"))
rule='[a-zA-z.]*[/d]*@gmail.com'
for lines in f1:
    mail = lines.rstrip("\n")
    matcher = fullmatch(rule,mailid)
    if matcher == None:
        print("invalid mail id")
    else:
        f2.write(mail)
print(f2)