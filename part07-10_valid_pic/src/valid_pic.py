# Write your solution here

from datetime import datetime, timedelta
import string

def is_it_valid(pic: str):

    if not check_date(pic):
        return False
    if not control_check(pic):
        return False
    if len(pic) != 11:
        return False
    return True


def is_leap_year(year):
    # A year is a leap year if:
    # 1. It's divisible by 4
    # 2. It's not divisible by 100, unless it is also divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def control_check(pic: str):

    check = (pic[10])
    #alph_list = (list(string.ascii_uppercase))
    #alph_str = ''.join(alph_list)
    #num_list = (list(map(str, range(9))))
    #num_str = ''.join(num_list)
    code_list = ("0123456789ABCDEFHJKLMNPRSTUVWXY")
    

    nine_digit = int(pic[0:6]+pic[7:10])
    d = nine_digit%31

    c = code_list[d]

    if code_list[d] == check:
        return True
    else:
        return False



def check_century(pic: str):
    cent_marker = pic[6]
    
    if cent_marker not in  ("+", "-", "A"):
        return False
    if cent_marker == "+":
        cent = 1800
    elif cent_marker == "-":
        cent = 1900
    elif cent_marker == "A":
        cent = 2000
    
    return cent



def check_date(pic: str):
    day = int(pic[:2])
    month = int(pic[2:4])
    year= (pic[4:6])
    #year_str = str(year)

    cent = check_century(pic)
    cent_str = str(cent)
    dob_year = int((cent_str[0:2])+(year))


    leap = is_leap_year(dob_year)

    if month > 12:
        return False

    elif month in (1, 3,5, 7, 8, 10, 12):
        if day > 31:
            return False
    elif month not in (1, 3,5, 7, 8, 10, 12):
        if day > 30:
            return False
    if not leap:
        if month == 2 and day>28:
            return False
    if cent == "A":
        dif = year-datetime.now().year
        
        if dif >0:
            return False
    return True


if __name__ == "__main__":
        
    checkN = ['290531+1054']#, "120488+246L", "310823A9877"]

    for a in checkN:
        result = is_it_valid(a)
        print(result)

       