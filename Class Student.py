class Student:

    count= 0
    total_gpa = 0
     
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return (f"{self.name} = {self.gpa}")
    
    @classmethod

    def average_gpa(cls):
        return f"Average gpa: {cls.total_gpa / cls.count:.2f}  "

    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
student1 = Student("Patrick", 3.2)
student2 = Student("Osman", 4.0)
student3 = Student("Hasan", 1.2)
    
print(Student.average_gpa())
print(Student.get_count(Student))
