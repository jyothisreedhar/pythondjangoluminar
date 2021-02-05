class Employee:
    def __init__(self, eid, name, desig, exp, salary):
        self.eid = eid
        self.name = name
        self.desig = desig
        self.exp = exp
        self.salary = salary

    def __str__(self):
        return self.name


f = open("employees", "r")
emp_list = []
sal_list = []
desig_list = []
for lines in f:
    eid, name, desig, exp, salary = lines.rstrip("\n").split(",")
    emp_list.append(Employee(eid, name, desig, exp, salary))
    print(emp_list)
