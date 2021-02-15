
from re import *
pattern="[a-zA-Z]"#will check for lowercase and upper case
matcher=finditer(pattern,"abc _72K@c")
for match in matcher:
    print(match.start())
    print(match.group())