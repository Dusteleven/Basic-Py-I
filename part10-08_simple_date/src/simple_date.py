# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year > another.year:
            return False
        elif self.month < another.month:
            return True
        elif self.month > another.month:
            return False
        elif self.day < another.day:
            return True
        elif self.day > another.day:
            return False
        else: return False

    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year < another.year:
            return False
        elif self.month > another.month:
            return True
        elif self.month < another.month:
            return False
        elif self.day > another.day:
            return True
        elif self.day < another.day:
            return False
        else: return False

    def __eq__(self, another):
        if self.year == another.year and self.month == another.month and self.day == another.day:
            return True
        else: return False


    def __ne__(self, another):
        if self.year != another.year or self.month != another.month or self.day != another.day:
            return True
        else: return False

    def __add__ (self, days):

        
        w_years = days //360
        if w_years > 0:
            w_days = days %360
        else: w_days = days

        w_months = w_days // 30
        w_days  = w_days %30

        new_year = self.year + w_years
        new_month = self.month + w_months
        new_day = self.day + w_days

        if new_day > 30:
            new_month +=1
            new_day -= 30
        if new_month > 12:
            new_year +=1
            new_month -= 12
    
        return SimpleDate(new_day, new_month, new_year)


    def __sub__ (self, another):
        years = self.year - another.year
        months = self.month - another.month
        days = self.day - another.day

        day_sum = (years*360)+ (months*30)+days

        if day_sum <0:
            day_sum *= -1
        return day_sum




if __name__ == "__main__":

    sdate = SimpleDate(5, 5, 1900)
    print(sdate + 20)

