num=input("enter the num:")#2
i=1
data=0
pattern=""
while(i<=int(num)):#1<=2
    res=(num*i)
    pattern=pattern+"+"+res
    print(res,"+",end='')
    print(rstrip(res))
    data+=int(res)
    i+=1
    pattern=pattern.lstrip("+")
    print(pattern)
print("=",data)