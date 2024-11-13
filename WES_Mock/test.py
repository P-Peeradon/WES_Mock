import unittest
from datetime import date
from enrolment import Enrolment
from student import Student
from unit import Unit
from staff import Staff

"""
This is the unit test for Student, Unit, Enrolment and Staff class
"""

class TestStudent(unittest.TestCase):
    
    def test_Student_constructor(self):
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
        stu1 = Student("18036024", "A", "Smith", date(2002, 5, 7), 
            "Master of Artificial Intelligence", "0390215032", "smith.a@gmail.com", 
            "24 Golder Str, Sydney, NSW 2000")
        stu2 = Student("20637053", "B", "Smith", date(2000, 12, 6), 
            "Master of Data Science", "0370536012", "smith.b@gmail.com", 
            "16 Barrakat Ln, Sydney, NSW 2000")
        stu3 = Student()
        
        #get ID
        self.assertEqual(stu1.get_id(), "18036024")
        self.assertEqual(stu2.get_id(), "20637053")
        self.assertEqual(stu3.get_id(), "00000000")
        #get first name
        self.assertEqual(stu1.get_fname(), "A")
        self.assertEqual(stu2.get_fname(), "B")
        self.assertEqual(stu3.get_fname(), "no name")
        #get last name
        self.assertEqual(stu1.get_lname(), "Smith")
        self.assertEqual(stu2.get_lname(), "Smith")
        self.assertEqual(stu3.get_lname(), "no surname")
        #get date of birth
        self.assertEqual(stu1.get_date_of_birth(), date(2002, 5, 7))
        self.assertEqual(stu2.get_date_of_birth(), date(2000, 12, 6))
        self.assertEqual(stu3.get_date_of_birth(), date(2000, 1, 1))
        #get program
        self.assertEqual(stu1.get_program(), "Master of Artificial Intelligence")
        self.assertEqual(stu2.get_program(), "Master of Data Science")
        self.assertEqual(stu3.get_program(), "unknown")
        #get phone number
        self.assertEqual(stu1.get_phone(), "0390215032")
        self.assertEqual(stu2.get_phone(), "0370536012")
        self.assertEqual(stu3.get_phone(), "03XXXXXXXX")
        #get email
        self.assertEqual(stu1.get_email(), "smith.a@gmail.com")
        self.assertEqual(stu2.get_email(), "smith.b@gmail.com")
        self.assertEqual(stu3.get_email(), "XXX@hotmail.com")
        #get address
        self.assertEqual(stu1.get_address(), "24 Golder Str, Sydney, NSW 2000")
        self.assertEqual(stu2.get_address(), "16 Barrakat Ln, Sydney, NSW 2000")
        self.assertEqual(stu3.get_address(), "unknown")
    
    def test_Student_setter(self):
        stu3 = Student()
        #Before
        self.assertEqual(stu3.get_id(), "00000000")
        self.assertEqual(stu3.get_fname(), "no name")
        self.assertEqual(stu3.get_lname(), "no surname")
        self.assertEqual(stu3.get_date_of_birth(), date(2000, 1, 1))
        self.assertEqual(stu3.get_program(), "unknown")
        self.assertEqual(stu3.get_phone(), "03XXXXXXXX")
        self.assertEqual(stu3.get_email(), "XXX@hotmail.com")
        self.assertEqual(stu3.get_address(), "unknown")
        
        #Use setter
        stu3.set_id("11802605")
        stu3.set_fname("C")
        stu3.set_lname("Johnson")
        stu3.set_date_of_birth(date(2001, 10, 5))
        stu3.set_program("Master of Information System")
        stu3.set_phone("0480256314")
        stu3.set_email("johnson.c@hotmail.com")
        stu3.set_address("402 Temple Str, Sydney, NSW 2000")
        
        #After
        self.assertEqual(stu3.get_id(), "00000000")
        self.assertEqual(stu3.get_fname(), "no name")
        self.assertEqual(stu3.get_lname(), "no surname")
        self.assertEqual(stu3.get_date_of_birth(), date(2000, 1, 1))
        self.assertEqual(stu3.get_program(), "unknown")
        self.assertEqual(stu3.get_phone(), "03XXXXXXXX")
        self.assertEqual(stu3.get_email(), "XXX@hotmail.com")
        self.assertEqual(stu3.get_address(), "unknown")
        

if __name__ == "__main__":
    unittest.main()