from animals import Animal
from interfaces import IFreshwater, ISwimming, ISaltwater

class RiverDolphin(Animal, IFreshwater, ISwimming, ISaltwater):
    instances = []

    def __init__(self, age, name):
        Animal.__init__(self)
        IFreshwater.__init__(self)
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        self.instances.append(self)
        self.name = name
        self.species = "River Dolphin"
        self.min_release_age = 13
        self.age = age
        self.prey = [ "trout", "mackarel", "salmon", "sardine" ]

    def feed(self, prey):
        if prey in self.prey:
            print(f'{self.name} the {self.species} ate {prey} for a meal')
        else:
            print(f'{self.name} the {self.species} rejects the {prey}')

    def move(self):
        print(f"The {self.species} swims")