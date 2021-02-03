employee = {
    1000: {"id": 1000, "name": "tom", "salary": 25000, "exp": 1},
    1001: {"id": 1001, "name": "jhon", "salary": 30000, "exp": 2},
    1002: {"id": 1002, "name": "danie", "salary": 35000, "exp": 2},
    1003: {"id": 1003, "name": "jack", "salary": 30000, "exp": 2}
}


def print_employee(**kwargs):
    # print(kwargs)
    id = kwargs["id"]#id=1000
    if id in employee:#1000 in emplouee
        print(employee[id]["name"])#tom
        if 'prop' in kwargs:
            prop = kwargs["prop"]#prop=exp
            print(employee[id][prop])
        else:
            pass
    else:
        print("employee with this id not exist")


print_employee(id=1000,prop="exp")
