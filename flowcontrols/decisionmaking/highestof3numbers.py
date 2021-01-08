num1=int(input("enter num1"))

num2=int(input("enter num2"))
num3=int(input("enter num3"))
if ((num1 > num2)&(num1 > num3)):
    print("num1 is large")

elif((num2 > num1)&(num2 > num3)):
    print("num2 is large")
elif((num3 > num1)&(num3 > num2)):
    print("num3 is large")

elif((num1 == num2)&(num1 == num3)):
    print("3 numbers are equal")

