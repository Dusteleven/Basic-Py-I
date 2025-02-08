# Write your solution here

def remove_smallest(numbers: list):
    print(numbers)
    numbers.remove(min(numbers))
    print(numbers)



if __name__ == "__main__":

    numbers = [1,2,3,4,5,6] 

    print(remove_smallest(numbers))
