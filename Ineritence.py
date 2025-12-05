class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def talk(self):
        print("Helloo")

class worker(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary= salary

    def work(self):
        self.talk()
        print("Im also working")

w = worker("aravind",12,12000)
w.work()