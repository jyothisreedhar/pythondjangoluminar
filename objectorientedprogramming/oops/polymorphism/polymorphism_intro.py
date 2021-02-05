# polymorphism
# meaning of polymorphism is many forms or more than one form
#polymorphism allow us to perform a single action in different ways
# method overloading
# method overriding
# operator overloading


# method overloading
# same method different number of arguments

class Maths:
    def add(self):
        print("inside no arg")

    def add(self, num1):
        print("inside one arg")

    def add(self, num1, num2):
        print("inside two arg")


m = Maths
m.add(10)
m.add(10, 20, 90)




# only recently implemented method working
