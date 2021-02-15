class Students:
    def __init__(self, rolno, name, course, total):
        self.rolno = rolno
        self.name = name
        self.course = course
        self.total = total

    def __str__(self):  # str is used for string representaion of object
        return self.name


obj = Students(100, "akshay", "django", 140)
obj1 = Students(101, "akhil", "mean", 140)
obj2 = Students(102, "ashi", "django", 145)
stud_list = []
stud_list.append(obj)
stud_list.append(obj1)
stud_list.append(obj2)
total = 0
for stud in stud_list:

     if stud.course == "django":
        print(stud.name)

# find django students total
        total += stud.total
print(total)
