y = int(input("Year:"))
ny = y+1


while True:
    if ny%4==0 and ny%100!=0 or ny%400==0:
        print(f"The next leap year after {y} is {ny}")
        break 
    ny +=1
    
