from WES_Mock.staff import Staff

class Unit:
    
    """
    Class that store unit data.
    unitcode (str) the code of that unit.
    unitname (str) the name of that unit
    unitdesc (str) the description of that unit. (Can be null)
    credit (integer) the credit point of that unit. 
    duration (float) the time (in hours) per week to complete the course.
    coordinator (Staff) the unit's coordinator. (Can be null)
    """
        
    def __init__(self, unitcode: str = "XXXXXXX", unitname: str = "Unknown", unitdesc: str = "", credit: int = 0, duration: float = 0.0, coordinator: Staff = Staff()):
        self.__unitcode = unitcode
        self.__unitname = unitname
        self.__unitdesc = unitdesc
        self.__credit = credit
        self.__duration = duration
        self.__coordinator = coordinator
        
    def get_unitcode(self) -> str:
        """
        Accessor method to get unitcode
        Return: unitcode of that unit. 
        """
        return self.__unitcode
    
    def get_unitname(self) -> str:
        """
        Accessor method to get unitname
        Return: name of that unit.
        """
        return self.__unitname
    
    def get_unitdesc(self) -> str:
        """
        Accessor method to get unitdesc
        Return: description of that unit.
        """
        return self.__unitdesc
    
    def get_credit(self) -> int:
        """
        Accessor method to get credit
        Return: credit for that unit.
        """
        return self.__credit
    
    def get_duration(self) -> float:
        """
        Accessor method to get duration
        Return: duration of all classes per one week for that subject, which student are required to take.
        """
        return self.__duration
    
    def get_coordinator(self) -> Staff:
        """
        Accessor method to get class coordinator
        Return: coordinator for that subject, whom student has to contact to in case of problems.
        """
        return self.__coordinator
    
    def set_unitcode(self, new_unitcode: str) -> None:
        """
        Mutator method to set new unitcode
        Parameter: new unitcode
        """
        self.__unitcode = new_unitcode
    
    def set_unitname(self, new_unitname: str) -> None:
        """
        Mutator method to set new unitname
        Parameter: new unitname
        """
        self.__unitname = new_unitname
    
    def set_unitdesc(self, new_unitdesc: str) -> None:
        """
        Mutator method to set new unit description
        Parameter: new unit description
        """
        self.__unitdesc = new_unitdesc
    
    def set_credit(self, new_credit: int) -> None:
        """
        Mutator method to set new credit point
        Parameter: new credit point
        """
        self.__credit = new_credit
    
    def set_duration(self, duration: float) -> None:
        """
        Mutator method to set new duration (hours per week)
        Parameter: new duration
        """
        self.__duration = duration
        
    def set_coordinator(self, new_coordinator: Staff) -> None:
        """
        Mutator method to set new class coordinator
        Parameter: new coordinator
        """
        self.__coordinator = new_coordinator
    
    def __str__(self):
        return f"Unit Code: {self.__unitcode} \nName: {self.__unitname} \
            \nDescription: {self.__unitdesc} \nCredits: {self.__credit} \
            \nHours per week: {self.__duration} \nCoordinator: {self.__coordinator}
            "