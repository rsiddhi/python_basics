class A:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def displayNumbers(self):
        print('Number 1: ' + str(self.num1))
        print('Number 2: ' + str(self.num2))

class B(A):
    def __init__(self, num1, num2):
        super().__init__(num1,num2)

    def displayNumbers(self):
        print('num1 = ' + str(self.num1) + ' num2 = ' + str(self.num2))


a = A(1,5)
print('Parent displayNumbers')
a.displayNumbers()

b = B(1,5)
print('Child displayNumbers, overriden')
b.displayNumbers()


class Vector:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(1,4)
print(v1+v2)


