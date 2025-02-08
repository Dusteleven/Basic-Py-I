n=int(input("Number: "))
t=0
f=0

if n%3==0:
    t = 1 
if n%5==0:
    f = 1 
if t and f:
    print("FizzBuzz")
elif t:
    print('Fizz')
elif f:
    print("Buzz")

