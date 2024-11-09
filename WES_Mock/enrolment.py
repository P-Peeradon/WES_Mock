from student import Student
from unit import Unit
from datetime import date

class Enrolment:
    
    def __init__(self, enrol_date: date = date(2019, 1, 1), unit: Unit = Unit(), student: Student = Student(), semester: int = 1, year: int = 2019):
        self.__enrol_date = enrol_date
        self.__unit = unit
        self.__student = student
        self.__semester = semester
        self.__year = year