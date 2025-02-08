# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week: int, winning_numbers:list):
        self.week = week
        self.winning_numbers = winning_numbers


    def number_of_hits(self, numbers: list):
        return len([n for n in numbers if n in self.winning_numbers])
    
    def hits_in_place(self, numbers:list):
        return [n if n in self.winning_numbers else -1 for n in numbers]