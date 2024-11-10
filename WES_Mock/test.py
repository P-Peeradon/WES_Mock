import unittest
from datetime import date
from enrolment import Enrolment
from student import Student
from unit import Unit

class TestStudent(unittest.TestCase):
    
    student1 = Student("012348023", "Mr.A", date(2002, 5, 7), )
    student2 = Student("080249033", "Mr.B", date(2002, 3, 20), )
    student3 = Student()
    
    def test_Student_getter(self):
        pass