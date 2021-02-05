class Book:
    def __init__(self,pages):
        self.pages = pages

    def __mul__(self, other):
        return Book(self.pages * other.pages)

    def __str__(self):
        return str(self.pages)
obj=Book(10)
obj1=Book(5)
print(obj*obj1)