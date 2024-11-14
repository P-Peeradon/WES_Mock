from datetime import date

class Staff:
    
    """
    Class that store UTS staff data.
    id (str) is the staff ID.
    fname (str) is the staff first name.
    lname (str) is the staff last name.
    address (str) is the staff's address in Australia.
    phone (str) is the student's telephone number.
    payment (float) is the staff payment per month in Australian Dollar (Denoted by A$).
    """
    
    def __init__(self, id: str = "0000-0000-0000-0000", fname: str = "no name", \
            lname: str = "no surname", address: str = "unknown",  \
            phone: str = "03XXXXXXXX", email: str = "XXX@hotmail.com", \
            payment: float = 0.00):
        self.__id = id
        self.__fname = fname
        self.__lname = lname
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__payment = payment
    
    @staticmethod
    def __connect_staff_db(self):
        raise NotImplementedError("Not implemented yet since no means to connect to database")
        
    def get_id(self) -> str:
        """
        Accessor method to get staff ID
        Return: Staff ID of that staff member.
        """
        return self.__id
    
    def get_fname(self) -> str:
        """
        Accessor method to get staff first name
        Return: first name of that staff member.
        """
        return self.__fname
    
    def get_lname(self) -> str:
        """
        Accessor method to get staff last name
        Return: last name of that staff member.
        """
        return self.__lname
    
    def get_phone(self) -> str:
        """
        Accessor method to get staff phone number
        Return: phone number of that staff member.
        """
        return self.__phone
    
    def get_address(self) -> str:
        """
        Accessor method to get staff address
        Return: address of that staff member. (In Australia)
        """
        return self.__address
    
    def get_email(self) -> str:
        """
        Accessor method to get staff email
        Return: official email of that staff member.
        """
        return self.__email
    
    def get_payment(self) -> float:
        """
        Accessor method to get staff payment
        Return: salary of that staff member in Australian dollar (A$).
        """
        return self.__payment
    
    def set_id(self, new_id: str) -> None:
        """
        Mutator method to set new staff ID
        Parameter: new staff ID for that staff member.
        """
        self.__id = new_id
    
    def set_fname(self, new_fname: str) -> None:
        """
        Mutator method to set new staff first name
        Parameter: new first name for that staff member.
        """
        self.__fname = new_fname
        
    def set_lname(self, new_lname: str) -> None:
        """
        Mutator method to set new staff last name
        Parameter: new last name for that staff member.
        """
        self.__lname = new_lname
        
    def set_phone(self, new_phone: str) -> None:
        """
        Mutator method to set new staff phone number
        Parameter: new phone number for that staff member.
        """
        self.__phone = new_phone
    
    def set_address(self, new_address: str) -> None:
        """
        Mutator method to set new staff address
        Parameter: new address for that staff member.
        """
        self.__address = new_address
    
    def set_email(self, new_email: str) -> None:
        """
        Mutator method to set new staff email
        Parameter: new official email for that staff member. (@uts.edu.au)
        """
        self.__email = new_email
    
    def set_payment(self, new_payment) -> float:
        """
        Mutator method to set new staff payment
        Parameter: new salary for that staff member in Australian dollar (A$). 
        """
        self.__payment = new_payment
    
    def __str__(self):
        """
        Method to convert Staff into String.
        return: String representation of Staff (For testing the code).
        """
        return f"staff ID: {self.__id} \nname: {self.__fname + ' ' + self.__lname} \
            \nphone: {self.__phone} \naddress: {self.__address} \
            \nemail: {self.__email} \npayment: A${self.__payment:.2f}"