num = input("enter the number:")  # 3 given num in format of string
i = 1
data = 0
pattern = "+"
while (i <= int(num)):  # 1<=3,2<=3,3<=3
    res = num * i  # 3'*i='3','3'*2='33','3'*3='333',
    pattern = pattern + "+" + res  # +3,+3+33,+3+33+333
    data = int(res)
    i += 1  # i=2,i=3,i=4
pattern = pattern.lstrip("+")
print(pattern)
print("=", data)
