from datetime import date
import mysql.connector as sql_conn

class Student():
    
    """
    Class that store student data.
    id (str) is the student ID.
    fname (str) is the student first name.
    lname (str) is the student last name.
    date_of_birth (DOB) is the student date of birth.
    phone (str) is the student's telephone number.
    address (str) is the student's address in Australia.
    """
        
    def __init__(self, id: str = "00000000", fname: str = "no name", lname: str = "", date_of_birth: date = date(2000, 1, 1), program: str = "unknown", phone: str = "03XXXXXXXX", email: str = "XXX@hotmail.com", address: str = "unknown"):
        self.__id = id
        self.__fname = fname
        self.__lname = lname
        self.__date_of_birth = date_of_birth
        self.__program = program
        self.__phone = phone
        self.__email = email
        self.__address = address
        
    """
        stu_db = sql_conn.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )
        
        stu_curr = stu_db.cursor()
    """
        
    def get_id(self) -> str:
        return self.__id
    
    def get_fname(self) -> str:
        return self.__fname 
    
    def get_lname(self) -> str:
        return self.__lname 
    
    def get_date_of_birth(self) -> date:
        return self.__date_of_birth
    
    def get_program(self) -> str:
        return self.__program
    
    def get_phone(self) -> str:
        return self.__phone
    
    def get_email(self) -> str:
        return self.__email
    
    def get_address(self) -> str:
        return self.__address
        
    def set_id(self, new_id: str) -> None:
        self.__id = new_id
    
    def set_fname(self, new_fname: str) -> None:
        self.__fname = new_fname
        
    def set_lname(self, new_lname: str) -> None:
        self.__lname = new_lname
    
    def set_date_of_birth(self, new_date_of_birth: date) -> None:
        self.__date_of_birth = new_date_of_birth
    
    def set_program(self, new_program: str) -> None:
        self.__program = new_program
    
    def set_phone(self, new_phone: str) -> None:
        self.__phone = new_phone
    
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    
    def set_address(self, new_address: str) -> None:
        self.__address = new_address
        