num=int(input("enter the num"))
res=0
while(num>0):
    digit=num%10
    res=res+digit**3
    num=num//10
if (num==res):
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")
print(res)
    