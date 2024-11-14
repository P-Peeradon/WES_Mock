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
        self.assertEqual(stu3.get_id(), "11802605")
        self.assertEqual(stu3.get_fname(), "C")
        self.assertEqual(stu3.get_lname(), "Johnson")
        self.assertEqual(stu3.get_date_of_birth(), date(2001, 10, 5))
        self.assertEqual(stu3.get_program(), "Master of Information System")
        self.assertEqual(stu3.get_phone(), "0480256314")
        self.assertEqual(stu3.get_email(), "johnson.c@hotmail.com")
        self.assertEqual(stu3.get_address(), "402 Temple Str, Sydney, NSW 2000")

class TestStaff(unittest.TestCase):
    
    def test_Staff_constructor(self):
        sf1 = Staff("1986-5000-4516-9021", "Several", "Snape", "84 Collins St, Canberra CBD, ACT 2600", "0384752142", "s.snape@uts.edu.au", 1480.50)
        sf2 = Staff("9547-8021-6021-9458", "David", "Griffindor", "1555/4 Canton Rd, Bondi Beach, NSW 2026", "0472601503", "d.griffindor@uts.edu.au", 2450.00)
        sf3 = Staff()
        
        print(sf1)
        print()
        print(sf2)
        print()
        print(sf3)
        
    def test_Staff_getter(self):
        sf1 = Staff("1986-5000-4516-9021", "Several", "Snape", "84 Collins St, Canberra CBD, ACT 2600", "0384752142", "s.snape@uts.edu.au", 1480.50)
        sf2 = Staff("9547-8021-6021-9458", "David", "Griffindor", "1555/4 Canton Rd, Bondi Beach, NSW 2026", "0472601503", "d.griffindor@uts.edu.au", 2450.00)
        sf3 = Staff()
        
        #get ID
        self.assertEqual(sf1.get_id(), "1986-5000-4516-9021")
        self.assertEqual(sf2.get_id(), "9547-8021-6021-9458")
        self.assertEqual(sf3.get_id(), "0000-0000-0000-0000")
        #get first name
        self.assertEqual(sf1.get_fname(), "Several")
        self.assertEqual(sf2.get_fname(), "David")
        self.assertEqual(sf3.get_fname(), "no name")
        #get last name
        self.assertEqual(sf1.get_lname(), "Snape")
        self.assertEqual(sf2.get_lname(), "Griffindor")
        self.assertEqual(sf3.get_lname(), "no surname")
        #get address
        self.assertEqual(sf1.get_address(), "84 Collins St, Canberra CBD, ACT 2600")
        self.assertEqual(sf2.get_address(), "1555/4 Canton Rd, Bondi Beach, NSW 2026")
        self.assertEqual(sf3.get_address(), "unknown")
        #get phone number
        self.assertEqual(sf1.get_phone(), "0384752142")
        self.assertEqual(sf2.get_phone(), "0472601503")
        self.assertEqual(sf3.get_phone(), "03XXXXXXXX")
        #get email
        self.assertEqual(sf1.get_email(), "s.snape@uts.edu.au")
        self.assertEqual(sf2.get_email(), "d.griffindor@uts.edu.au")
        self.assertEqual(sf3.get_email(), "XXX@hotmail.com")
        #get payment
        self.assertEqual(sf1.get_payment(), 1480.50)
        self.assertEqual(sf2.get_payment(), 2450.00)
        self.assertEqual(sf3.get_payment(), 0.00)
        
    def test_Staff_setter(self):
        sf3 = Staff()
        
        #before
        self.assertEqual(sf3.get_id(), "0000-0000-0000-0000")
        self.assertEqual(sf3.get_fname(), "no name")
        self.assertEqual(sf3.get_lname(), "no surname")
        self.assertEqual(sf3.get_address(), "unknown")
        self.assertEqual(sf3.get_phone(), "03XXXXXXXX")
        self.assertEqual(sf3.get_email(), "XXX@hotmail.com")
        self.assertEqual(sf3.get_payment(), 0.00)
        
        #call setter method
        sf3.set_id("1405-9452-1450-7581")
        sf3.set_fname("Ron")
        sf3.set_lname("Wesley")
        sf3.set_address("84 Rosecoe Str, Bondi Beach, NSW 2026")
        sf3.set_phone("0301154062")
        sf3.set_email("r.wesley@uts.edu.au")
        sf3.set_payment(4750.25)
        
        #after
        self.assertEqual(sf3.get_id(), "1405-9452-1450-7581")
        self.assertEqual(sf3.get_fname(), "Ron")
        self.assertEqual(sf3.get_lname(), "Wesley")
        self.assertEqual(sf3.get_address(), "84 Rosecoe Str, Bondi Beach, NSW 2026")
        self.assertEqual(sf3.get_phone(), "0301154062")
        self.assertEqual(sf3.get_email(), "r.wesley@uts.edu.au")
        self.assertEqual(sf3.get_payment(), 4750.25)

class testUnit(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()