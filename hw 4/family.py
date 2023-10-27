class Family:
    def __init__(self, age:float, name:str, surname:str, status:str):
        self.Age:float = age
        self.Name:str = name
        self.Surname:str = surname
        self.Status:str = status
    def __str__(self):
        return (f'Name - {self.Name}\n'
                f'Surname - {self.Surname}\n'
                f'Status - {self.Status}\n'
                f'Age - {self.Age}')