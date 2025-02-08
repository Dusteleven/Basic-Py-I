# Write your solution here

def read_input(s: str, a: int, b: int):
    while True:
        try:
            num=int(input(f"{s}"))
        
        except ValueError:
            print(f"You must type in an integer between {a} and {b}")
            continue
        
            
            
        if num>a and num<b:

            return (int(num))
        else:
            print(f"You must type in an integer between {a} and {b}")

        
    


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)