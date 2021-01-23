def comon_ltrs():
    str1=input(("enetr string one:"))
    str2=input(("enetr string one:"))
    st1=set(str1)
    st2=set(str2)
    str3=set(str1).intersection(set(str2))
    print("common lettres are:",str3)
comon_ltrs()