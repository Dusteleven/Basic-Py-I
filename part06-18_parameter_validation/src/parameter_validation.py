# Write your solution here


def new_person(name: str, age: int):

    if (name==""or len(name.split(" "))<2 or len(name)>40 or age<0 or age >150):
        raise ValueError ("check params")
    else:
        r=(name, age)
        return (r)

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)