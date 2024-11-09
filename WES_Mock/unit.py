class Unit:
        
    def __init__(self, unitcode: str = "XXXXXXX", unitname: str = "Unknown", unitdesc: str = "", credit: int = 0, duration: float = 0.0):
        self.__unitcode = unitcode
        self.__unitname = unitname
        self.__unitdesc = unitdesc
        self.__credit = credit
        self.__duration = duration
        
    def get_unitcode(self) -> str:
        return self.__unitcode
    
    def get_unitname(self) -> str:
        return self.__unitname
    
    def get_unitdesc(self) -> str:
        return self.__unitdesc
    
    def get_credit(self) -> int:
        return self.__credit
    
    def get_duration(self) -> float:
        return self.__duration
    
    def set_unitcode(self, new_unitcode: str) -> None:
        self.__unitcode = new_unitcode
    
    def set_unitname(self, new_unitname: str) -> None:
        self.__unitname = new_unitname
    
    def set_unitdesc(self, new_unitdesc: str) -> None:
        self.__unitdesc = new_unitdesc
    
    def set_credit(self, new_credit: int) -> None:
        self.__credit = new_credit
    
    def set_duration(self, duration: float) -> None:
        self.__duration = duration
    