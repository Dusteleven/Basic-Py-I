# Write your solution here

from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    a= (leg1*leg1)
    b=(leg2*leg2)
    c=(sqrt(a+b))

    return(c)

if __name__ == "__main__":
    hypotenuse(1.0, 3.0)