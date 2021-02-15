from re import *
phn_num=int(input("enter the number"))
#rule="[0-9]{10}"
rule='(91)?\d{10}'#91 is optional

match = fullmatch(rule, phn_num)
if match == None:
    print("invalid phone number number")
else:
    print("valid phone number number")
