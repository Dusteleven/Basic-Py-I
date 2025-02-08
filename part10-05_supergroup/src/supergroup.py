# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'
    

class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []


    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    @name.setter
    def name(self, name:str):
        self._name = name

    @location.setter
    def location(self, location:str):
        self._location = location


    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def __str__(self):
        return(f"{self._name}, {self._location}")

    def print_group(self):
        print(self)
        print(f"Members:")
        for p in self._members:
            print(p)

