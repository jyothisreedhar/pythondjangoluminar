from re import *
pattern="[A-Z]" #will check for uppercase A to Z
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())