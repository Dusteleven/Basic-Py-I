p = int(input("How many points [0-100]: "))
if p<0 or p>100:
    a = "impossible!"
elif p<=49:
    a = "fail"
elif p<=59:
    a = 1
elif p<=69:
    a = 2
elif p<=79:
    a = 3
elif p<=89:
    a = 4
else:
    a = 5
print(f"Grade: {a}")
