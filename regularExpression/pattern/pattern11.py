from re import *

# pattern = "a{2,4}"  # minimum 2 number of a maximum 4 number of a
pattern = "a{2,4}"
matcher = finditer(pattern, "abaaaaaaabababaaa")
for match in matcher:
    print(match.start(), "==>", match.group())
