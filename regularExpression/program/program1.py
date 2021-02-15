#a,,k first character must be a alphabet including a-k
#second must be a number divisible by 3
#followed by any number of character
#eg:a9ui

from re import *
var_name=input("enter variable name")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,var_name)
if matcher == None:
    print("invalid variable name")
else:
    print('valid variable')