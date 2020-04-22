from animals import Animal
from interfaces import ITerrestrial, Identifiable, IFlying

class Opeapea(Animal, ITerrestrial, Identifiable, IFlying):

    def __init__(self, age, name):
        Animal.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.name = name
        self.__species = "Opeapea"
        self.__min_release_age = 5
        self.age = age
        self.__prey = { "Ants", "Fly", "Grass", "Plants"}


    @property
    def prey(self):
        return self.__prey

    @property 
    def species(self):
        return self.__species

    @property
    def min_release_age(self):
        return self.__min_release_age

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The bat ate {prey} for a meal')
        else:
            print(f'The bat rejects the {prey}')

    def move(self):
        print(f"The {self. species} flies")

    def __str__(self):
        return f'Opeapea {self.id}'