# Write your solution here
from datetime import datetime, timedelta



def date_list(start_date, days):
    day_list = []
    new_date = start_date
    add_day = timedelta(days=1)

    for i in range(int(days)):
        day_list.append(new_date)
        new_date += add_day
        
    return day_list


if False:
    file_name = "late_june.txt"
    start_date = datetime.strptime(("24.6.2020"), "%d.%m.%Y")
    days = "1"
else:
    file_name = input("Filename: ")
    start_date = datetime.strptime((input("Starting date: ")), "%d.%m.%Y")
    days = input("How many days: ")
    print("please type in screen time in minutes on each day (TV computer mobile):")

day_list = date_list(start_date, days)
day_hours_list = {}
hours_total=0

for day in day_list:
    hours = (input(f"Screen time {day}: "))
    hours_split = hours.split(" ")
    for b in hours_split:
        hours_total += int(b)
    
    day_hours_list[day]=hours_split

avg_mins = hours_total/ int(days)

with open(file_name, "w") as new_file:
    new_file.write(f"Time period: {day_list[0].strftime("%d.%m.%Y")}-{day_list[len(day_list)-1].strftime("%d.%m.%Y")}\n")
    new_file.write(f"Total minutes: {hours_total}\n")
    new_file.write(f"Average minutes: {avg_mins}\n")
    for d, h in day_hours_list.items():
        new_file.write(f"{d.strftime("%d.%m.%Y")}: {h[0]}/{h[1]}/{h[2]}\n")

print(f"Data stored in file {file_name}")





