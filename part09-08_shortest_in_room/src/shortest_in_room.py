# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    

class Room:
    def __init__ (self):
        self.persons = []


    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else: return False
    
    def print_contents(self):
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortestperson = Person
            shortestheight = 100000000
            for p in self.persons:
                if p.height < shortestheight:
                    shortestperson = p
                    shortestheight = p.height
            return shortestperson
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            
            shortP = self.shortest()
            self.persons.pop(self.persons.index(shortP))
            return shortP















if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

