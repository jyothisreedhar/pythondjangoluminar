# multilevel inheritance


class Parent:
    def m1(self):
        print("inside parent")
    # def new(self):
    # print("hello")


class Child(Parent):
    def m2(self):
        print("inside child")


class SubChild(Child):
    def m3(self):
        print("inside Sub Child")


obj = SubChild()
obj.m3()
obj.m2()
obj.m1()
# obj.new()
