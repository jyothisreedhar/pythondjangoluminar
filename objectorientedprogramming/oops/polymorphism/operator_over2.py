class Book:
    def __init__(self, pages):
        self.pages = pages

    def __sub__(self, other):
        return Book(self.pages - other.pages)

    def __str__(self):
        return str(self.pages)


obj = Book(200)
obj1 = Book(100)
print(obj-obj1)
