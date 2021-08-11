# =========================
# OOP 0.1
# =========================
#  multi inheriting
class A:

    def do(self):
        print('In A')


class B(A):
    pass


class C:
    def do(self):
        print('In C')


class D(B, C):
    pass


ob = D()
ob.do()
print(D.mro())  # class mro = Show plan inheriting

# --------------------
# example 2
# --------------------


class Student:

    def __init__(self, name):
        self.marks = []
        print(f'Welcome {name}')

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_avg(self):
        avg = sum(self.marks)/len(self.marks)
        print(avg)


s1 = Student('AhmedSelim')

s1.add_mark(30)
s1.add_mark(50)
s1.add_mark(20)
s1.add_mark(90)


s1.get_avg()













