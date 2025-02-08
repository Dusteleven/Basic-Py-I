# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, a: str, b: str):
        if len(a) < len(b):
            return 2
        elif len(a) == len(b):
            return 0
        else: return 1



class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, a: str, b: str):
        vowels = ["a", "e", "i", "o", "u"]
        p1vow = 0 
        p2vow = 0

        for letter in a:
            if letter in vowels:
                p1vow+=1

        for letter in b:
            if letter in vowels:
                p2vow+=1

        if p1vow >p2vow:
            return 1
        elif p2vow > p1vow:
            return 2
        elif p1vow == p2vow:
            return 0
        else: return 0  

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, a: str, b: str):
        words = ['rock', 'paper', 'scissors']

        if a in words and b in words:
            if a == 'rock' and b == 'scissors':
                return 1
            elif a == 'rock' and b == 'paper':
                return 2 
            elif a == 'rock' and b == 'rock':
                return 0
            elif a == 'paper' and b == 'scissors':
                return 2
            elif a == 'paper' and b == 'rock':
                return 1 
            elif a == 'paper' and b == 'paper':
                return 0
            elif a == 'scissors' and b == 'paper':
                return 1
            elif a == 'scissors' and b == 'rock':
                return 2 
            elif a == 'scissors' and b == 'scissors':
                return 0
        
        elif a not in words and b not in words:
            return 0

        elif b not in words:
            return 1
        elif a not in words:
            return 2

        else: return 0
    
if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()