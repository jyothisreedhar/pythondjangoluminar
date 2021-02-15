# print employee details whose designation developer
# no of employees as a developer
# print employee details who have highest salary
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


# printing high salary of employee

    for employee in emp_list:
        sal_list.append(employee.salary)
print(max(sal_list))

# print lowest salary of developer

    for employee in emp_list:
        if desig=="developer":
            desig_list.append(employee.salary)

print(min(desig_list))

# print employee details whose designation developer

#devop=list(filter(lambda emp:emp.desig=="developer",emp_list))
#print(devop)
