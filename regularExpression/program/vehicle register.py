# validate vehicle reg:no
# kl 2 digit 2 alphabet 4 digit
from re import *

reg_name = input("enter registration num:")
# rule="kl[0-9][0-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]"
# rule = 'kl[0-9]{2}[a-zA-Z]{2}\d{4}'
rule = 'kl\d{2}[a-zA-Z]{2}\d{4}'
match = fullmatch(rule, reg_name)
if match == None:
    print("invalid registration number")
else:
    print("valid registration number")
