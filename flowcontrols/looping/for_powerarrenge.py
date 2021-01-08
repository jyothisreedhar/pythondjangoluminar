num=int(input('num:'))#2
lwlimit=int(input('lwlimit:'))#4
uplimit=int(input('uplimit:'))#30
for i in range(1,uplimit+1):
    if i**num in range(lwlimit,uplimit):
        print(i)
