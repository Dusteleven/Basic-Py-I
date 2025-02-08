y=int(input("Please type in a year:"))

a= (y%4==0)
b= (y%100==0)
c= (y%400==0)


if (a and b and c):
    print("That year is a leap year.")
elif a and not b:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
