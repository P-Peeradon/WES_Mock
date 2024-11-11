from WES_Mock.enrolment import Enrolment
from WES_Mock.unit import Unit
from WES_Mock.student import Student

class Transaction:
    
    MAX_CREDIT_PER_SEMESTER = 24
    
    def __init__(self, student: Student, trans_num: str = "U0000000000000", semester: int = 1, year: int = 2019):
        self.__trans_num = trans_num
        self.__student = student
        self.__units: Unit = []
        self.__semester = semester
        self.__year = year
    
    def sum_credit(self):
        """
        This method will sum the credit in that semester
        """
        #Get unit from the enrolment data and sum all credit first
        raise NotImplementedError("This method is not implemented")