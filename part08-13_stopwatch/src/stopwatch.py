# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds <=58:
            self.seconds+=1
        elif self.minutes <=58:
            self.seconds=0
            self.minutes+=1
        else:
            self.seconds = 0
            self.minutes = 0
    
    def __str__ (self):
        if self.seconds<10:
            sec = (f"0{self.seconds}")
        else: sec = self.seconds

        if self.minutes <10:
            min = (f"0{self.minutes}")
        else: min = self.minutes

        return(f"{min}:{sec}")
    



