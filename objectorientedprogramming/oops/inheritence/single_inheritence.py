class Parent():
    def phone(self):
        print("i have nokia435")


class Child(Parent):  # child inherited from parent
    pass


c = Child()
#print(c)
c.phone()