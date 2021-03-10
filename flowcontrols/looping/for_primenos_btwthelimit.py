lwlimit=int(input('lwlimit')) #10
uplimit=int(input('uplimit')) #50
for num in range(lwlimit,uplimit+1):#(10,51)
    if num>1: #10>1
        flag=0
        for i in range(2,num) #(2,10):
            if(num%i==0):
                flag+=1
                break
        if flag==0:
            print(num)