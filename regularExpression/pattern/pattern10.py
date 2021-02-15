from re import *

# pattern="\s" #will check for spaces
# pattern="\d" #will check for digits
#pattern = "\D"  # will check except digit
#pattern="\w" #will check for all words except special charecters
pattern="\W" #will check except words

matcher = finditer(pattern, "abc _7ZK@c")
for match in matcher:
    print(match.start(),"-->",match.group())
    #print(match.group())
