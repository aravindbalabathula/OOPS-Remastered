class Employee:

    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age 
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)

class manager:
    
    def update(obj):
        obj.salary += 1000 
        obj.display() 


e = Employee("Aravind",22,10000)
manager.update(e)
