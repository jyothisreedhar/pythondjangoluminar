from re import *

pattern = '[ab]'  # it will check either a or b
matcher = finditer(pattern, "abc _7Z@kc")
for match in matcher:
    print(match.start())  # 0 1
    print(match.group())  # a b
