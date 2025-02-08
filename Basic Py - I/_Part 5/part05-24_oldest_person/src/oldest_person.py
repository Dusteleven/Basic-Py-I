# Write your solution here

def oldest_person(people: list):

    dumYear = people[0][1]
    name=people[0][0]
    for t in people:
        if t[1]<dumYear:
            dumYear=t[1]
            name=t[0]
    return name







if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))