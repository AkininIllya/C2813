class Animal:
    def __init__(self, name: str, age: float, color: str, country: str, breed: str):
        self.Name: str = name
        self.Age = age
        self.Color = color
        self.Breed = breed
        self.Country = country

    def __bool__(self):
        return self.Name != None and \
            self.Age != None and \
            self.Color != None and \
            self.Breed != None and \
            self.Country != None

    def __len__(self):
        return len(self.Name)

    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n"
                f"Color - {self.Color}\n"
                f"Breed - {self.Breed}\n"
                f"Country - {self.Country}")

