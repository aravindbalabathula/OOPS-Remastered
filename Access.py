class A:

    def __init__(self):
        self.__a = 30
        self._b = 100

    def __what(self):
        print(self.__a)

a = A()
a.a = 40
print(a.a)
a._A__what()
print(a._b)

