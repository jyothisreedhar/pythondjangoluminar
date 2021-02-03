class Employee:
    def __init__(self,id,name,desig):
        self.id=id
        self.name=name
        self.desig=desig
    def print_employee(self):
        print(self.name,self.id,self.desig)

obj=Employee(101,"vijay","mca")
obj.print_employee()