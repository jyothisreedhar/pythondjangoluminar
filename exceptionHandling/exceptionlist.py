lst = [10, 20, 30]
position = int(input("enter the position to print element"))  # 10
try:
    print(lst[position])  # 0
except:
    print("invalid position")
