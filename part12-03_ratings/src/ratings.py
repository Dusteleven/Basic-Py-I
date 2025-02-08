# TEE RATKAISUSI TÄHÄN:

def sort_by_ratings(items: list):

    def order_by_ratings(i:dict):
        return i["rating"]
    
    return sorted(items, key=order_by_ratings, reverse=True)