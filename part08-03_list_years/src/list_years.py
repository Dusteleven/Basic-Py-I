# Write your solution here
# Remember the import statement
# from datetime import date


from datetime import date

def list_years(dates: list):
    yearList = []
    for d in dates:
        yearList.append(d.year)
    yearList = sorted(yearList)




    return yearList
