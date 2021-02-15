from re import *
pattern="[a-zA-Z0-9]" #will check for all word except underscore and space
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())