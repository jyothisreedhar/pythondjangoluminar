employee = {
    1000: {"id": 1000, "name": "tom", "salary": 25000, "exp": 1},
    1001: {"id": 1001, "name": "jhon", "salary": 30000, "exp": 2},
    1002: {"id": 1002, "name": "danie", "salary": 35000, "exp": 2},
    1003: {"id": 1003, "name": "jack", "salary": 30000, "exp": 2}
}


def print_employee(**kwargs):
    print(kwargs)  # {'id': 1000, 'prop': 'salary'}
    id = kwargs["id"]  # print kwargs dict id value
    if id in employee:
        print(employee[id]["name"])
    else:
        print("employee id doesnt exist")


print_employee(id=1000, prop="salary")


#def print_employee(id=None, prop=None):
   # if id in employee:
       # print(employee[id][prop])
#    else:
      #  print("employee id doesnt exist")


#print_employee(id=1000, prop="salary")

# def print_employee(id=None):
#  if id in employee:
#      print(employee[id]["name"])
#   else:
#    print("employee id does not exist")
# print_employee(id=1000)

# print(employee[1000])  # {"id": 1000, "name": "tom", "salary": 25000, "exp": 1},

# print name of employee who have id=1001

#if 1001 in employee:
  #  print(employee[1001]["name"])
#else:
   # print('employee id doesnt exist')
#
# print salary of emply id 1003

if 1003 in employee:
    print(employee[1003]["salary"])
else:
    print('employee id doesnt exist')
