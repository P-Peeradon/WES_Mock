from datetime import date

class Staff:
    
    def __init__(self, id: str = "", name: str = "no name", address: str = "unknown", email: str = "XXX@hotmail.com", payment: float = 0.00):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__payment = payment
        
    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_address(self) -> str:
        return self.__address
    
    def get_email(self) -> str:
        return self.__email
    
    def get_payment(self) -> float:
        return self.__payment
    
    def set_id(self, new_id: str) -> None:
        self.__id = new_id
    
    def set_name(self, new_name: str) -> None:
        self.__name = new_name
    
    def set_address(self, new_address: str) -> None:
        self.__address = new_address
    
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    
    def set_payment(self, new_payment) -> float:
        self.__payment = new_payment