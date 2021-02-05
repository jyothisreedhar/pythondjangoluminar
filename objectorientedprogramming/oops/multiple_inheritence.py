class Parent:
    def m1(self):
        print("inside parent")


class Child:
    def m1(self):
        print("inside child")


class SubChild(Child,Parent):
    def m3(self):
        print("inside subchild")


obj = SubChild()
obj.m3()
obj.m1()  # it will check first m1 method is in subchild
# if no it will  check the m1 method in child
# if yes print that or no check the m1 method in parent
