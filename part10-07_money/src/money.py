# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents<10:
            return f"{self.__euros}.0{self.__cents} eur"     
        elif self.__cents >=10:
            return f"{self.__euros}.{self.__cents} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents


    def __gt__(self, another):
        if self.__euros > another.__euros:
            return True
        elif self.__euros < another.__euros:
            return False
        elif self.__euros == another.__euros:
            if self.__cents > another.__cents:
                return True
            elif self.__cents < another.__cents:
                return False
            return False
        
    def __lt__(self, another):
        if self.__euros < another.__euros:
            return True
        elif self.__euros > another.__euros:
            return False
        elif self.__euros == another.__euros:
            if self.__cents < another.__cents:
                return True
            elif self.__cents > another.__cents:
                return False
            return False
        

    def __ne__(self, another):
        return  self.__euros != another.__euros or self.__cents != another.__cents




    def __add__ (self, another):


        sum_euros = self.__euros + another.__euros 
        sum_cents = self.__cents + another.__cents
        if sum_cents >=100:
            sum_euros+=1
            sum_cents -= 100

        return Money(sum_euros, sum_cents)
    

    def __sub__ (self, another):
        
        #if another.euros < self.euros or (another.euros == self.euros and another.cents < self.cents):
            sum_euros = self.__euros - another.__euros 
            try_cents = self.__cents - another.__cents
            if try_cents <0:
                sum_euros -=1
                sum_cents = try_cents +100
            else: sum_cents = try_cents
            if sum_euros < 0:
                raise ValueError("A negative result is not allowed")
            return Money(sum_euros, sum_cents)
             
                


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1


