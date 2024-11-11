from WES_Mock.enrolment import Enrolment
from WES_Mock.unit import Unit
from WES_Mock.student import Student
import random

class Transaction:
    
    MAX_CREDIT_PER_SEMESTER = 24
    
    def __init__(self, student: Student, trans_num: str = "U0000000000000", semester: int = 1, year: int = 2019):
        self.__trans_num = trans_num
        self.__student = student
        self.__units: Unit = []
        self.__semester = semester
        self.__year = year
        
    def generate_trans_num(self) -> str:
        trans_num = "U"
        for i in range(13):
            #since random.randint() return int, we have to cast str type.
            trans_num += str(random.randint(0, 9))
        
        #This is called when submit the transaction and the transaction is completed.
        return trans_num
        
    
    def sum_credit(self):
        """
        This method will sum the credit in that semester
        """
        #Get unit from the enrolment data and sum all credit first
        #Then sum credit of all unit in this transaction
        raise NotImplementedError("This method is not implemented")