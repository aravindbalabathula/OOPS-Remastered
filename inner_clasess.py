class Outer:

    def __init__(self):
        print("outer invoked")

    class Inner:

        def __init__(self):
            print("Iinnter initiated")

        def m1(self):
            print("Helli broo")

o = Outer()
i = o.Inner()
i.m1()