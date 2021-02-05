class student:
    def set_StudId(self, rolno, age, name, course):
        self.rolno = rolno  # instance variable
        self.age = age
        self.name = name
        self.course = course

    def get_StudId(self):
        print(self.rolno, self.name, self.course, self.age)


obj = student()
obj.set_StudId("rollno:20\n", "name:jyothi\n", "course:engineering\n", "age: 22\n")
obj.get_StudId()
# set_student is initializing instance variable
# instance variables are variables that cane be prepended with self keyword
# we can access instance variable outside class by using reference
# we can access instance variable inside class by using self keyword
# constructor
# ------------------------
#
