# =================================
# Example OOP
# =================================
class Calculator:
    def __init__(self , name):  # constructor Auto run
        print(f'Welcome {name}')

    def sum(self, x, y):  # self  = Booking Space for Object (c1, v1, ...)
        result = 1
        print(x + y)
        return x + y

    def sub(self, x, y):
        print(x - y)
        return x - y


class Sic(Calculator):
    def power(self , x, y):
        print(x**y)

c1 = Calculator('Ahmed')  # The parameter can be sent in the class.
c1.sum(2, 3)
# ----------------------------------
v1 = Calculator('Mostafa')  # The parameter can be sent in the class.
v1.sum(10, 2)
v1.sub(100, 70)
# ----------------------------------
c1.result = 1001
print(c1.result)
# ----------------------------------
# del c1.result  # delete value  Attribute
# ----------------------------------
a1 = Sic('a')
a1.power(2, 3)
a1.sum(3, 4)
# ----------------------------------