#read the students and failed students file and create passedf students list
#----------------------------
stud1=open("students","r")#read the student file
stud2=open("fail","r")#read faild std list
st1=set(stud1)#convert it in to set
st2=set(stud2)
#print(st1,st2)
passtd=st1.difference(st2)#take the diff of 2 set to get the passdtd lis
print("passd students:",passtd)

#for lines in passtd:
 #   print(lines)





