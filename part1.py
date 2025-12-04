class Student:
    '''This class is developed by B. Aravind'''

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def info(self):
        print("Name is: ", self.name)
        print("Marks are is: ", self.marks)
        print("Roll No are: ", self.rollno)


student_DB = []

while True:
    name = input("Enter the name of the Student : ")
    rollNo = input("Enter the roll number : ")
    marks = int(input("Enter the marks : "))
    s = Student(name,rollNo,marks)
    student_DB.append(s)
    print("Continue [Y/N] : ")
    k = input()
    if k.lower() == "y":
        continue
    else:
        break

for i in student_DB:
    i.info()