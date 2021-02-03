#kwargs
#recive numbers of arguments in the form of tuple using *

def add(*args):
    return sum(args)
total=add(10,20,30,50)
print(total)

#recive numbers of arguments in the form of dict using**

def print_data(**kwargs):
    print(kwargs)
print_data(name="jyo",worklocation="kasaragod",home="periya")
