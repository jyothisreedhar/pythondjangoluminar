def shuf_strg():
    str1 = input(("enetr string one:"))
    str2 = input(("enetr string two:"))
    str1=str1+str2
    print(len(str1))
    print(len(str2))
    str2=str1[0:len(str1)-len(str2)]
    str1=str1[len(str2): ]
    print("reversed string is:",str1,str2)
shuf_strg()
