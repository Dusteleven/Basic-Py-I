timesperweek = float(input("How many times a week do you eat at the student cafeteria?"))
lprice = float(input("The price of a typical student lunch?"))
gprice = float(input("How much money do you spend on groceries in a week?"))
print("")
dsum = (lprice*timesperweek + gprice)

print(f"Average food expenditure: ")
print(f"Daily: {dsum/7} euros")
print(f"Weekly: {dsum} euros")