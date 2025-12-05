# Car object Has-A  Engine reference

class Engine:

    def __init__(self):
        print("Engine ready")
    
    def start(self):
        print("Engine started and running")

class Car:

    def __init__(self):
        print("Car opened")
        self.e = Engine()

    def move(self):
        print("give ignition")
        self.e.start()
        print("Car smoving brooo...")

c = Car()
c.move()