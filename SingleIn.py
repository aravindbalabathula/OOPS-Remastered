class Father:
    def __init__(self):
        print("Im father")

    def walk(self):
        print("Im walking")

class son(Father):
    def __init__(self):
        print("Im son")
    

    def dancing(self):
        print("Im  dancing")

s = son()
s.walk()
s.dancing()

