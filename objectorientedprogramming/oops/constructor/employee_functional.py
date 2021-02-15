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

# printing employee details whose designation is developer

develop = list(filter(lambda emp: emp.desig == "developer", emp_list))
for emp in develop:
    print(emp)

# no of employees as a developer

cnt = len(list(filter(lambda emp: emp.desig == "developer", emp_list)))
print(cnt)

# print maximum salary

max_salary=max(list(map(lambda emp:emp.salary,emp_list)))
print(max_salary)

