employees = [
    {"eid": 10, "name": "christy", "desig": "dataanalyst", "sal": 50000, "join": 1980, "resign": 1992},
    {"eid": 11, "name": "sabir", "desig": "developer", "sal": 54000, "join": 1985, "resign": 1990},
    {"eid": 12, "name": "chris", "desig": "developer", "sal": 30000, "join": 1989, "resign": 1995},
    {"eid": 13, "name": "nath", "desig": "bca", "sal": 38000, "join": 1999, "resign": 2016}
]

# print highest salary of employee

salary = list(map(lambda emp: emp['sal'], employees))
print(salary)
max_salary = max(map(lambda emp: emp['sal'], employees))
print(max_salary)

# print employee names whose experience greater than 10yrs
# exp_name=list(filter(lambda emp:emp['name] if (emp['resign']-emp['join'])>10,employees))
# print(exp_name)


exp_name = list(filter(lambda emp: (emp["resign"] - emp["join"]) > 10, employees))
print(exp_name)
