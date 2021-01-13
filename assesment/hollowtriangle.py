n=int(input("enter the value of n:"))#5
for row in range(n):#(0,5)
    for col in range(n-int(row)):#(5-0=5),4

        print(".",end="")#printing 5 space before the star,4

    for col in range(int(2*row+1)):#(2*0+1=1),3

        if (col==0)|(col==2*row)|(row==n-1):()

            print("*",end="")

        else:
            print("-",end="")

    print()
    #print(hello0