from datetime import date
import mysql.connector as sql_conn

class Student():
    
    """
    Class that store student data.
    id (str) is the student ID.
    fname (str) is the student first name.
    lname (str) is the student last name.
    date_of_birth (date) is the student date of birth.
    phone (str) is the student's telephone number.
    email (str) is the student's personal email. (No university domain)
    address (str) is the student's address in Australia.
    """
    
    #name of the table, if need to retrieve data from database.
    DB_TABLE_NAME = "student"
        
    def __init__(self, id: str = "00000000", fname: str = "no name" \
            , lname: str = "no surname", date_of_birth: date = date(2000, 1, 1) \
            , program: str = "unknown", phone: str = "03XXXXXXXX" \
            , email: str = "XXX@hotmail.com", address: str = "unknown"):
        self.__id = id
        self.__fname = fname
        self.__lname = lname
        self.__date_of_birth = date_of_birth
        self.__program = program
        self.__phone = phone
        self.__email = email
        self.__address = address    
        
    def get_id(self) -> str:
        """
        Accessor method to get student id
        Return: ID of that student.
        """
        return self.__id
    
    def get_fname(self) -> str:
        """
        Accessor method to get student first name
        Return: first name of that student.
        """
        return self.__fname 
    
    def get_lname(self) -> str:
        """
        Accessor method to get student last name
        Return: last name of that student.
        """
        return self.__lname 
    
    def get_date_of_birth(self) -> date:
        """
        Accessor method to get student date of birth
        Return: DOB of that student.
        """
        return self.__date_of_birth
    
    def get_program(self) -> str:
        """
        Accessor method to get student's program
        Return: program name which that student is studying
        """
        return self.__program
    
    def get_phone(self) -> str:
        """
        Accessor method to get student phone number
        Return: that student's phone number
        """
        return self.__phone
    
    def get_email(self) -> str:
        """
        Accessor method to get student's email
        Return: that student's email. 
        """
        return self.__email
    
    def get_address(self) -> str:
        """
        Accessor method to get student's address
        Return: that student's address. 
        """
        return self.__address
        
    def set_id(self, new_id: str) -> None:
        """
        Mutator method to set student's id
        Parameter: New student ID.
        """
        self.__id = new_id
    
    def set_fname(self, new_fname: str) -> None:
        """
        Mutator method to set student's first name
        Parameter: New student first name.
        """
        self.__fname = new_fname
        
    def set_lname(self, new_lname: str) -> None:
        """
        Mutator method to set student's last name
        Parameter: New student last name.
        """
        self.__lname = new_lname
    
    def set_date_of_birth(self, new_date_of_birth: date) -> None:
        """
        Mutator method to set student's date of birth
        Parameter: New student date of birth (In case we key incorrect data).
        """
        self.__date_of_birth = new_date_of_birth
    
    def set_program(self, new_program: str) -> None:
        """
        Mutator method to set student's program
        Parameter: New student program.
        """
        self.__program = new_program
    
    def set_phone(self, new_phone: str) -> None:
        """
        Mutator method to set student's phone number
        Parameter: New student phone number.
        """
        self.__phone = new_phone
    
    def set_email(self, new_email: str) -> None:
        """
        Mutator method to set student's email
        Parameter: New student email.
        """
        self.__email = new_email
    
    def set_address(self, new_address: str) -> None:
        """
        Mutator method to set student's address
        Parameter: New student address. (Must be address in Australia. I will implement method to check format later on)
        """
        self.__address = new_address
        
    def __str__(self):
        """
        Method to convert Student into String.
        return: String representation of Student (For testing the code).
        """
        return f"id: {self.__id} \nname:{self.__fname + ' ' + self.__lname} \
            \nDOB: {self.__date_of_birth.strftime('%-d %B %Y')} \nprogram: {self.__program} \n \
            phone: {self.__phone} \nemail: {self.__email} \naddress: {self.__address}"



