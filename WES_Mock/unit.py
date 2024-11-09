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