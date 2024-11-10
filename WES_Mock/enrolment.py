from student import Student
from unit import Unit
from datetime import date

class Enrolment:
    
    def __init__(self, enrol_date: date = date(2019, 1, 1), units: Unit = [], student: Student = Student(), semester: int = 1, year: int = 2019):
        self.__enrol_date = enrol_date
        self.__units = units
        self.__student = student
        self.__semester = semester
        self.__year = year
        
    def get_enrol_date(self) -> date: 
        return self.__enrol_date
    
    def get_units(self) -> Unit:
        return self.__units
    
    def get_specific_units(self, index: int)-> Unit:
        if index >= len(self.__units):
            raise IndexError("Index out of bound")
        else:
            return self.__units[index]
    
    def get_student(self) -> Student:
        return self.__student
    
    def get_semester(self) -> int:
        return self.__semester
    
    def get_year(self) -> int:
        return self.__year