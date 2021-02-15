from re import *

pattern = "ab"
matcher = finditer(pattern, "abababababbbbbabababbbbaababab")
# print(matcher)
cnt = 0
for match in matcher:
    print(match.start())  # print/return position
    print(match.group())  # group the sequence
    cnt += 1
print(cnt)
