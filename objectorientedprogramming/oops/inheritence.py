# inheritance
# -----------
# inheritance allow us to define a class that inherits all the methods and properties from another clas
# parent class===>it is the base class
# child class===>it is the derived class


class Parent():
    def phone(self):
        print("i have nokia435")


class Child(Parent):  # child inherited from parent
    pass


c = Child()
print(c)  # hexadecimal value of location
c.phone()

# different types of inheritance
# parent==>child
# super==>sub
# base==>derived
