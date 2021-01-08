num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if ((num1 > num2)&(num1 > num3)):
    print("num1 is large")
    if (num2>num3):
        print('num2 is the second largest')
    else:
        print('num3 is the second largest')
elif((num2 > num1)&(num2 > num3)):
    print("num2 is large")
    if(num3>num1):
        print('num3 is the second largest')
    else:
        print('num1 is the second largest')
elif((num3 > num1)&(num3 > num2)):
    print("num3 is large")
    if(num1>num2):
        print('num1 is the second largest')
    else:
        print('num2 is the second largest')


elif((num1 == num2)&(num1 == num3)):
    print("3 numbers are equal")
