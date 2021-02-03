class employee:
    def Set_Employee(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def get_Employee(self):
        print(self.id,self.name,self.designation,self.salary)
obj=employee()
obj1=employee()
obj.Set_Employee("id=101\n","name=manu\n","designation=mca\n","salary=50000\n")
obj.get_Employee()
obj1.Set_Employee("id=106\n","name=vinu\n","designation=bca\n","salary=30000\n")
obj1.get_Employee()