num=int(input('enter the num'))#123
#res=0
res=""
while(num>0):
    digit=num%10#123%10#3
    #res=res*10+digit
    res=res+str(digit)
    print(digit,end='')
    num=num//10#12

