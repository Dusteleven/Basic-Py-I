# Write your solution here


def even_numbers(beginning: int, maximum:int):
    n=beginning if beginning % 2 ==0 else beginning +1

    while n<= maximum:
        yield n
        n+=2

if __name__ == "__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)