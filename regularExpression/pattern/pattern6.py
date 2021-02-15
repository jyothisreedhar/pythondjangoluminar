from re import *
pattern="[0-9]"#will check for digits
matcher=finditer(pattern,"abc _72K@c")
for match in matcher:
    print(match.start())
    print(match.group())