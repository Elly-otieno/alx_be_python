class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        print(f"{self.name} is {self.age} years old")


my_student = Student('Lucy', 12)
my_student.student_info()