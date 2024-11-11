from datetime import date

class Staff:
    
    """
    Class that store UTS staff data.
    id (str) is the staff ID.
    fname (str) is the staff first name.
    lname (str) is the staff last name.
    address (str) is the staff's address in Australia.
    phone (str) is the student's telephone number.
    payment (float) is the staff payment per month in A$.
    """
    
    def __init__(self, id: str = "0000-0000-0000-0000", fname: str = "no name", lname: str = "", phone: str = "03XXXXXXXX", address: str = "unknown", email: str = "XXX@hotmail.com", payment: float = 0.00):
        self.__id = id
        self.__fname = fname
        self.__lname = lname
        self.__phone = phone
        self.__address = address
        self.__email = email
        self.__payment = payment
        
    def get_id(self) -> str:
        return self.__id
    
    def get_fname(self) -> str:
        return self.__fname
    
    def get_lname(self) -> str:
        return self.__lname
    
    def get_phone(self) -> str:
        return self.__phone
    
    def get_address(self) -> str:
        return self.__address
    
    def get_email(self) -> str:
        return self.__email
    
    def get_payment(self) -> float:
        return self.__payment
    
    def set_id(self, new_id: str) -> None:
        self.__id = new_id
    
    def set_fname(self, new_fname: str) -> None:
        self.__fname = new_fname
        
    def set_lname(self, new_lname: str) -> None:
        self.__lname = new_lname
        
    def set_phone(self, new_phone: str) -> None:
        self.__phone = new_phone
    
    def set_address(self, new_address: str) -> None:
        self.__address = new_address
    
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    
    def set_payment(self, new_payment) -> float:
        self.__payment = new_payment