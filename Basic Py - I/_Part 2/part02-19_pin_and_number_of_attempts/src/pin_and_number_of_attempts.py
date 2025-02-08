code=4321
count=0
while True:
    ans = int(input("PIN: "))
    count += 1
    if (ans == code) and (count >1):
        print(f"Correct! It took you {count} attempts")
        break
    elif ans == code and count ==1:
        print(f"Correct! It only took you one single attempt!")
        break
    else:
        print("Wrong")
    
