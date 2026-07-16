# a class called Student with name, age, marks attributes and a method called grade() 
# that returns A if marks > 90, B if > 80, C if > 70, F otherwise

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def grade(self):
        if self.marks >= 90 :
            return 'A'
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return 'C'
        else :
            return 'F'
s1=Student("Chintu",20,96)
print(s1.grade())

