class stud:
    def __init__(self):
        print("no arg constructor")

    def __init__(self, name, age):
        print("two arg constructor")


obj1 = stud()
obj1 = stud("tom", 45)

# only recently implemented constructor is working
# constructor overloading is not supported
