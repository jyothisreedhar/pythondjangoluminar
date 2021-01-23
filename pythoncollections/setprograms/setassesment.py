#?students=["name1","name2","name3","name3"]
#failed std=[name1 name2]
#create passed stdlst
students=["ajay","vijay","saji","suji","suji"]
stud=set(students)
#print(stud)
failstd=["ajay","saji"]
passedstd=stud.difference(failstd)

print("passed students",passedstd)