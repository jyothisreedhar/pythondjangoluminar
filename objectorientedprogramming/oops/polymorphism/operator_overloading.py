class Book:
    def __init__(self, pages):
        self.pages = pages

    #          obj    obj1

    def __add__(self, other):
        return Book(self.pages + other.pages)#100 200=300,300+300

    def __str__(self):
        return str(self.pages)


obj = Book(100)

# print(type(obj))

obj1 = Book(200)
obj2 = Book(300)

# print(obj + obj1) #+ operator can be used in numbers and strings

print(obj + obj1 )
print(obj+obj1+obj2)
