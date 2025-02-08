# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []
        self.count=0

    def add_number(self, number:int):
        self.numbers.append(number)
        self.count+=1
        pass

    def count_numbers(self):
        return self.count
        pass

    def get_sum(self):
        sum=0
        for i in self.numbers:
            sum+=i
        return sum
    
    def average(self):
        if self.count !=0:
            sum = self.get_sum()
            count = (self.count_numbers())
            avg = sum/count
            return avg
        else: return 0

new_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    int_input = int(input("Please type in integer numbers: "))
    if int_input != -1:
        new_stats.add_number(int_input)
        if int_input%2==0:
            even_stats.add_number(int_input)
        else:
            odd_stats.add_number(int_input)
    else:
        print(f"Sum of numbers: {new_stats.get_sum()}")
        print(f"Mean of numbers: {new_stats.average()}")
        print(f"Sum of even numbers: {even_stats.get_sum()}")
        print(f"Sum of odd numbers: {odd_stats.get_sum()}")
        break