hwage = float(input("Hourly wage: "))
hworked = int(input("Hours worked: "))
dow = input("Day of the week: ")
if dow != "Sunday":
    print(f"Daily wages: {hwage*hworked} euros")
else:
    print(f"Daily wages: {hwage*hworked*2} euros")