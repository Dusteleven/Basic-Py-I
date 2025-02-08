# Write your solution here:

def sort_by_remaining_stock(items: list):
    #name, price, remaining stock
    #sort by stock, lowest first

    def sort_by_stock(i:tuple):
        return i[2]
    
    return sorted(items, key=sort_by_stock)