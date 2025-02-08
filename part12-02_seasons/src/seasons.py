# Write your solution here:

def sort_by_seasons(items: list):

    def sort_by_s(i:dict):
        return i["seasons"]
    
    return sorted(items, key = sort_by_s)