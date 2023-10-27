from  animalrole import AnimalRole
class Animal:
    def __init__(self, name:str, breed:str, role:AnimalRole):
        self.Name:str = name
        self.Breed:str = breed
        self.Role:AnimalRole = role
    def __str__(self):
        return (f'Name - {self.Name}\n'
                f'Breed - {self.Breed}\n'
                f'Role - {self.Role.name}')
