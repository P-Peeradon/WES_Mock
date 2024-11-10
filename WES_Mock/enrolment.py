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
        
    def add_unit(self, unit: Unit) -> None:
        self.__units.append(unit)
        
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
    
    def remove_unit(self, unit: Unit) -> None:
        for idx in range(len(self.__units)):
            if self.__units[idx].get_unitcode() == unit.get_unitcode():
                self.__units()
                return
        
        raise ValueError("Cannot find unit")
    
    def set_enrol_date(self, new_enrol_date: date) -> None: 
        self.__enrol_date = new_enrol_date
    
    def set_units(self, new_units: Unit) -> None:
        self.__units = new_units
    
    def set_specific_units(self, index: int, unit: Unit = Unit()) -> None:
        if index >= len(self.__units):
            raise IndexError("Index out of bound")
        else:
            self.__units[index] = unit
    
    def set_student(self, new_student: Student) -> None:
        self.__student = new_student
    
    def set_semester(self, new_semester: int) -> None:
        self.__semester = new_semester
    
    def set_year(self, new_year: int) -> None:
        self.__year = new_year