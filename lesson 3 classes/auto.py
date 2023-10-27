from humanrole import HumanRole
from autotype import AutoType
from human import Human
from animal import Animal
from animalrole import AnimalRole
class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Passengers:list = list()
        self.Drivers:list = list()
        self.Cats:list = list()
        self.Dogs:list = list()
    def AddPassengers(self, human:Human):
        if(human.Role == HumanRole.PASSENGER):
            self.Passengers.append(human)
    def AddDrivers(self, human:Human):
        if(human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)

    def AddCats(self, animal:Animal):
        if(animal.Role == AnimalRole.CAT):
            self.Cats.append(animal)
    def AddDogs(self, animal:Animal):
        if(animal.Role == AnimalRole.DOG):
            self.Dogs.append(animal)

    def __str__(self):
        return (f'Passengers:\n ''.join(self.Passengers)\n'
                f'Drivers:\n ''.join(self.Drivers)\n'
                f'Cats:\n''.join(self.Cats)\n'
                f'Dogs:\n''.join(self.Dogs')