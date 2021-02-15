from re import *
gmail=input("enter mail id")
rule='[a-zA-z.]*[/d]*@gmail.com'
matcher = fullmatch(rule, gmail)
if matcher == None:
    print("invalid gmail id")
else:
    print("valid gmail id")
