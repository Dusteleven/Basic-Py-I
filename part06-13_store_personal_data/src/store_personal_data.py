# Write your solution here


def store_personal_data(person: tuple):
    w=(f"{person[0]};{person[1]};{person[2]}\n")

    with open("people.csv","a") as new_file:
        new_file.write(w)