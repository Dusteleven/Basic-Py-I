# Write your solution here:


class Item:

    def __init__ (self, name: str, weight: int):
        self.__name = name
        self.__weight = weight


    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__ (self):
        return (f"{self.__name} ({self.__weight} kg)")
    




class Suitcase:

    def __init__ (self, max_weight:float, items: list = None):
        self.__max_weight = max_weight
        if items is None:
            self.__items = []

    def add_item (self, item: "Item"):
        if self.__check_weight(item):
            self.__items.append(item)
        
    def __check_weight(self, item: "Item"):
        curr_w = self.weight()
        if (self.__max_weight - curr_w) >= item.weight():
            return True
        else: return False


    def weight(self):
        w = 0
        for i in self.__items:
            w+= i.weight()
        return w

    def __str__ (self):
        if len(self.__items) ==1:
            return (f"{len(self.__items)} item ({self.weight()} kg)")
        else:
            return  (f"{len(self.__items)} items ({self.weight()} kg)")

    def print_items(self):
        #if len(self.__items) > 0:
            #print ("The suitacase contains the following items:")
        for i in self.__items:
            print(f"{i.name()} ({i.weight()} kg)")
        #print (f"Combined weight: {self.weight()} kg")

    def heaviest_item(self):
        
        if len(self.__items)>0:
            hw = 0
            hi = ""
            for i in self.__items:
                if i.weight() > hw:
                    hw = i.weight()
                    hi = i
            return hi
        else: return None


class CargoHold:

    def __init__(self, max_weight: float, suitcases:list = None):
        self.__max_weight = max_weight
        if suitcases == None:
            self.__suitcases = []

    def add_suitcase(self, suitcase:"Suitcase"):
        if (self.__max_weight - self.__totalweight()) >= suitcase.weight():
            self.__suitcases.append(suitcase)

    def __qtycases(self):
        return len(self.__suitcases)
    
    def __totalweight(self):
        sum=0
        for i in self.__suitcases:
            sum+=i.weight()
        return sum


    def __str__ (self):
        if self.__qtycases() == 1:
            return (f"{self.__qtycases()} suitcase, space for {(self.__max_weight)-(self.__totalweight())} kg")
        else: 
            return (f"{self.__qtycases()} suitcases, space for {(self.__max_weight)-(self.__totalweight())} kg")

    def print_items(self):
        for item in self.__suitcases:
            item.print_items()




if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()