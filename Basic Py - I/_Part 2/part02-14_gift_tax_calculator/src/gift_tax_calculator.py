g=float(input("Value of gift:"))

if(g<5000):
    print("No tax!")
elif(g<=25000):
    print(f"Amount of tax: {100 + (g-5000)*0.08} euros")
elif(g<=55000):
    print(f"Amount of tax: {1700 + (g-25000)*0.1} euros")
elif(g<=200000):
    print(f"Amount of tax: {4700 + (g-55000)*0.12} euros")
elif(g<=1000000):
    print(f"Amount of tax: {22100 + (g-200000)*0.15} euros")
elif(g>1000000):
    print(f"Amount of tax: {142100 + (g-1000000)*0.17} euros")