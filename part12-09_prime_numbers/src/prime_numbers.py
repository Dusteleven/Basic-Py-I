# Write your solution here


def prime_numbers():
    n=2

    while True:
        prime = True
        if n == 2:
            yield n
            n+=1

        for i in range(2,n):
            if n%i == 0:
                prime=False
                break
            
        if prime:
            yield n
            n+=1
        else:
            n+=1
    


        
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))