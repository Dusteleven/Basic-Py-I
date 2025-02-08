# Write your solution here

import json


def print_persons(filename: str):

    with open(filename) as my_file:
        data= my_file.read()
        students = json.loads(data)
    
        for person in students:
            
            name = person["name"]
            age = str(person["age"]) + " years"
            hobbies = "(" + ", ".join(person["hobbies"]) + ")"

            print (f"{name} {age} {hobbies}")







if __name__ == "__main__":
    file = "file1.json"
    print_persons(file)