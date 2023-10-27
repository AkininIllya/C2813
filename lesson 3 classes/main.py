from auto import Human
from auto import Auto
from auto import AutoType
from auto import HumanRole
from auto import Animal
from auto import AnimalRole

humans = list()
yasin = Human('Yasin', HumanRole.DRIVER)
nikita = Human('Nikita', HumanRole.PASSENGER)
illya = Human('Illya', HumanRole.PASSENGER)
arsenii = Human('Arsenii', HumanRole.PASSENGER)
humans.append(yasin)
humans.append(nikita)
humans.append(illya)
humans.append(arsenii)

animals = list()
bobik = Animal('Bobik', 'Beagle', AnimalRole.DOG)
murzik = Animal('Murzik', 'British Shorthair', AnimalRole.CAT)
animals.append(bobik)
animals.append(murzik)

bmw = Auto("X6", AutoType.CAR)
for human in humans:
    bmw.AddPassengers(human)
    bmw.AddDrivers(human)

for animal in animals:
    bmw.AddCats(animal)
    bmw.AddDogs(animal)

for driver in bmw.Drivers:
    print(driver)
for passenger in bmw.Passengers:
    print(passenger)
for cat in bmw.Cats:
    print(cat)
for dog in bmw.Dogs:
    print(dog)

print(bmw)