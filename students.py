class Student:

    class_year = 2025
    num_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_student += 1
    
    def isim(self):
        print(self.name)

    def yaş(self):
        print(self.age)

