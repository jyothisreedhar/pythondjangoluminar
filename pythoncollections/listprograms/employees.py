employees = [
    [10, "christy", "dataanalyst", 50000],
    [11, "jhon", "ba", 30000],
    [12, "sab", "dataanalyst", 40000],
    [13, "tom", "developer", 40000],
    [14, "jhoni", "developer", 30000],
    [15, "sabir", "dataanalyst", 50000],
    [16, "tino", "developer", 40000],
    [17, "tomis", "developer", 47000],
    [18, "jhonis", "developer", 32000],
]
# print no of employees
number_of_employees = len(employees)
print("num of employees =", number_of_employees)
# print how much salary company has to raise in month end
total_amount = 0
for emp in employees:
    total_amount += emp[3]
print(total_amount)

# group by designation

d_count, da_analyst, ba_count = 0, 0, 0
for emp in employees:
    if emp[2] == "dataanalyst":
        da_analyst += 1
    elif emp[2] == "developer":
        d_count += 1
    elif emp[2] == "ba":
        ba_count += 1
print("dataanalyst", da_analyst, "ba_count ", ba_count, "developer ", d_count)

# print highest salaried employees name

salary_list = []
for emp in employees:
    salary_list.append(emp[3])
hig_salary = max(salary_list)
print(hig_salary)

# print employee name who receive lowest salary in designation=developer
salary_list = []
for emp in employees:
    salary_list.append(emp[3])
low_salary = min(salary_list)
for emp in employees:
    if (emp[2] == "developer") & (emp[3] == low_salary):
        print(emp)
