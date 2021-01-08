lwlimit=int(input('lwlimit'))
uplimit=int(input('uplimit'))
for num in range(lwlimit,uplimit+1):
    if num>1:
        flag=0
        for i in range(2,num):
            if(num%i==0):
                flag+=1
                break
        if flag==0:
            print(num)