st = input("Word: ")

buf = int((28-len(st))/2)
mod = (28-len(st))%2


if mod ==0:
    print(30*"*")
    print("*" + buf*" " + st+ buf*" " +"*")
    print(30*"*")
else:
    print(30*"*")
    print("*" + (buf+1)*" " + st+ buf*" " +"*")
    print(30*"*")
