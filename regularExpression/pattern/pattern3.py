from re import *

pattern = "[a-z]"  # check for lower case a-z
matcher = finditer(pattern, "abc _72K@c")
for match in matcher:
    print(match.start())
    print(match.group())
