from re import *
f1= open("phonenumber", "r")
f2= open("numbers", "w")
# phone_num=int(input("enter the phone number:"))
rule = '(91)?\d{10}'
for lines in f1:
    num = lines.rstrip("\n")
    #print(num)
    matcher = fullmatch(rule,num)
    if matcher == None:
        pass
    else:
        f2.write(num)
        f2.write('\n')

f2.close()
