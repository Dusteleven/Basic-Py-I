# Write your solution here


inp=input(("Whom should I sign this to: "))
sav=input("Where shall I save it: ")

with open(sav,"w") as new_file:
    new_file.write("Hi " +inp+ ", we hope you enjoy learning Python with us! Best, Mooc.fi Team")