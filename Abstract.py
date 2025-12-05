from abc import abstractmethod,ABC 

class A(ABC):

    def greet(self):
        print("Hello ")

    @abstractmethod
    def walk(self):
        pass 

class B(A):
    def walk(self):
        print("okay now walk")

a = B()
a.greet()
a.walk()
