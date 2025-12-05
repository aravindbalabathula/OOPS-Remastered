class A:
    def m1(self, *args):
        for i in args:
            print(i)

a = A()

a.m1(12,34,45,23,45,23)
a.m1("sdf","sdf","wsdfsdf")
a.m1(12,"sdf",32.4)