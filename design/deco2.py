def sub(num1, num2):
    return num1 - num2


def substract(func):
    def inner(num1, num2):
        if num1 < num2:
            (num1, num2) = (num2, num1)
        return func(num1, num2)

    return inner


@substract
def sub(num1, num2):
    return num1 - num2


data = sub(20, 100)
print(data)
