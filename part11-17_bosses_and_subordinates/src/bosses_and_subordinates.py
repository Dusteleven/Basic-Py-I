# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)



def count_subordinates(employee: Employee):

    if employee.subordinates is None:
        return 0

    scount = len(employee.subordinates)

    for e in employee.subordinates:
        scount += count_subordinates(e)
    return scount