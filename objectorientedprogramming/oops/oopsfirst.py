# class
# object
# reference
class Person:
    # methods
    def setPerson(self, age, name, ):
        self.age = age  # person has age
        self.name = name  # person has name

    def PrintPerson(self):
        print("age =", self.age)
        print("name =", self.name)


# created a class person
# attribute 0f a person is name,age ie,(self.name,self.age)
# setPerson and PrintPerson is a two method

obj = Person()
obj.setPerson(29, "jyothi")
obj.PrintPerson()
obj1 = Person()
obj1.setPerson(78, "narayan")
obj1.PrintPerson()
