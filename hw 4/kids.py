from family import Family

class Kids(Family):
    def __init__(self, age:float, name:str, surname:str, status:str):
        super().__init__(age, name, surname, status)
