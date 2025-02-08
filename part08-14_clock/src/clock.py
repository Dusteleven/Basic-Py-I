# Write your solution here:


class Clock:

    def __init__(self, hour: int, min: int, sec:int):
        self.sec = sec
        self.min = min
        self.hour = hour
    
    def __str__(self):
        s = Clock.singles(self.sec)
        m = Clock.singles(self.min)
        h = Clock.singles(self.hour)

        s=(f"{h}:{m}:{s}")
        return s
    
    def singles(num: int):
        if num <10:
            s = (f"0{num}")
            return s
        else: return num
    
    def tick(self):
        if self.sec <=58:
            self.sec+=1
        elif self.min<=58:
            self.min+=1
            self.sec=0
        elif self.hour <=22:
            self.hour+=1
            self.min = 0
            self.sec = 0
        else:
            self.hour = 0
            self.min = 0
            self.sec = 0

    def set(self, set_hour:int, set_min:int):
        self.hour = set_hour
        self.min = set_min
        self.sec = 0

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)