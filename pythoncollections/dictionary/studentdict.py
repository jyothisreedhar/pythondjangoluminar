# print name student rollno=1000
f = open("students", "r")
students = {}

for lines in f:#1000,tom,250,mca
    #print(lines)
    id, name, total, course = lines.rstrip("\n").split(",")
   #1000{nmae:ajay,course:mca,total=150}

    if id not in students:
        1000:{{"id":1000}}
        students[id] = {"id": id, "name": name, "total": total, "course": course}  # create nested dict


# print(students)

def print_student_data(**kwargs):
    id = kwargs["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwargs:
            prop = kwargs["prop"]
            print(students[id][prop])
    else:
        print("the id doesnot exist")

print_student_data(id="1000",prop="course")


