# Write your solution here

from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

mil = datetime(1999, 12,31)
userDate = datetime(year, month, day)

dif = mil-userDate
if dif.days > 0:
    print(f"You were {dif.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")