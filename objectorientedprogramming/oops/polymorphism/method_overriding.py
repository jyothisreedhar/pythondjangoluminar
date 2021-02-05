# method overriding
# method overriding can be existed in between two classes


class Parent:
    def mobile(self):
        print("nokia345")


class Child(Parent):
    def mobile(self):
        print("iphone12")


c = Child()
print(c)  # printing an object while printing object __str__()will invoke
c.mobile()
