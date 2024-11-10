from datetime import date

class Student():
        
    def __init__(self, id: str = "000000000", name: str = "no name", date_of_birth: date = date(2000, 1, 1), degree: str = "unknown", phone: str = "03XXXXXXXX", email: str = "XXX@hotmail.com", address: str = "unknown"):
        self.__id = id
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__degree = degree
        self.__phone = phone
        self.__email = email
        self.__address = address
        
    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name 
    
    def get_date_of_birth(self) -> date:
        return self.__date_of_birth
    
    def get_degree(self) -> str:
        return self.__degree
    
    def get_phone(self) -> str:
        return self.__phone
    
    def get_email(self) -> str:
        return self.__email
    
    def get_address(self) -> str:
        return self.__address
        
    def set_id(self, new_id: str) -> None:
        self.__id = new_id
    
    def set_name(self, new_name: str) -> None:
        self.__name = new_name
    
    def set_date_of_birth(self, new_date_of_birth: date) -> None:
        self.__date_of_birth = new_date_of_birth
    
    def set_degree(self, new_degree: str) -> None:
        self.__degree = new_degree
    
    def set_phone(self, new_phone: str) -> None:
        self.__phone = new_phone
    
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    
    def set_address(self, new_address: str) -> None:
        self.__address = new_address
        