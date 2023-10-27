from animal import Animal

class Cat(Animal):
    def __init__(self, age:float, nick:str, breed:str, sound:str):
        super().__init__(age, nick, breed, sound)
    def Speak(self):
        return self.Sound