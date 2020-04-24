from animals import Animal
from interfaces import ITerrestrial, IFlying

class Pueo(Animal, ITerrestrial, IFlying):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        IFlying.__init__(self)
        self.name = name
        self.species = "Pueo"
        self.min_release_age = 8
        self.age = age
        self.prey = { "Mouse", "Rat" }
        self.tolerate_shade = True
        self.tolerate_sun = True

    def feed(self, prey):
        if prey in self.prey:
            print(f'The owl ate {prey} for a meal')
        else:
            print(f'The owl rejects the {prey}')

    def move(self):
        print(f"The {self.species} flies")