import unittest
from datetime import date
from enrolment import Enrolment
from student import Student
from unit import Unit

class TestStudent(unittest.TestCase):
    
    stu1 = Student("18036024", "A", "Smith", date(2002, 5, 7), 
            "Master of Artificial Intelligence", "0390215032", "smith.a@gmail.com", 
            "24 Golder Str, Sydney, NSW 2000")
    stu2 = Student("20637053", "B", "Smith", date(2000, 12, 6), 
            "Master of Data Science", "0370536012", "smith.b@gmail.com", 
            "16 Barrakat Ln, Sydney, NSW 2000")
    stu3 = Student()
    
    print(stu1)
    print()
    print(stu2)
    print()
    print(stu3)
    
    def test_Student_getter(self):
        global stu1
        global stu2
        global stu3
        self.assertEqual(stu1.get_id())