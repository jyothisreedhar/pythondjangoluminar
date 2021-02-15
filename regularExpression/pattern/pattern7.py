from re import *
pattern="[^0-9]" #will check for except 0 to 9
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())