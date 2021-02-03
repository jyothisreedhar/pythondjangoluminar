class student:
    def set_student(self, rol, name, course):
        self.rol = rol
        self.name = name
        self.course = course

    def get_student(self):
        print(self.rol, ",", self.name, ",", self.course)


obj = student()
obj.set_student(10, "engineering", 'jyothi')
obj.get_student()
# print(obj.course)
# print(obj.rol)
