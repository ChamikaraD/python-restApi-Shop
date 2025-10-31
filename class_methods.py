from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Student:
    school: ClassVar[str] = 'Pelwatta' # class variable
    name :str
    age :int


    def print_student_info(self):
        print(f"name - {self.name} age ={self.age}")

    @staticmethod
    def ad_numbers(a:int ,b:int):
        print( a+ b)


    @classmethod
    def print_school(cls):
        print(cls.school)




#std1 = Student(name="test", age=20)

