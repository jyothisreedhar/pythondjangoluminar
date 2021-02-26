def sub(num1, num2):
    if num1<num2:
        (num1,num2)=(num2,num1)
    return num1 - num2
print(sub(18, 28))
