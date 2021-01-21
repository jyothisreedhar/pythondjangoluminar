employe={"id":100,"ename":"ajay","exp":2,"salary":35000}
if("salary" in employe):
    print(employe["salary"])
#print employe name
print(employe["ename"])
#gender
if("gender" in employe):
    print("exit")
else:
    employe["gender"]="male"
print(employe)
#if employe salary <35000 add 5000rs more
if (employe["salary"]<=35000):
    employe["salary"]+=5000
print(employe)
#COURSE
if ("course" in employe):
    print("exit")
else:
    employe["course"]="python"
print(employe)
#bonus
if("bonus" in employe):
    print("exit")
else:
    employe["bonus"]=5000
print(employe)
#pf
if ("pf" in employe):
    print("exit")
else:
    employe["pf"]=7000
print(employe)
#id
if("id" in employe):
    print("exit")
else:
    employe["id"]=101
print(employe)