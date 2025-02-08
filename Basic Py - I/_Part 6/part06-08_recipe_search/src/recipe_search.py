# Write your solution here

def file_cleaner(filename:str):

    full_list=[]
    part_list=[]
    dummy_list=[]
    with open(filename) as new_file:
        i=0
        for line in new_file:
            part_list.append(line.strip())
        
        for i in part_list:
            if i == "":
                full_list.append(dummy_list)
                dummy_list=[]
            else:
                dummy_list.append(i)
        full_list.append(dummy_list)

        for row in full_list:
            if row[0]=="":
                row.pop(0)

    return full_list



def search_by_name(filename: str, word: str):
    
    full_list = file_cleaner(filename)
    list_of_recipe_names=[]

    for row in full_list:
        if  word.lower() in row[0].lower():
            list_of_recipe_names.append(row[0])
        
    return list_of_recipe_names

def search_by_time(filename: str, prep_time: int):
    full_list = file_cleaner(filename)
    recipes_below_time=[]

    for row in full_list:
        if  int(row[1]) <= prep_time:
            recipes_below_time.append((f"{row[0]}, preparation time {row[1]} min"))

    return recipes_below_time


def search_by_ingredient(filename: str, ingredient: str):
    full_list = file_cleaner(filename)
    recipes_with_ingredient=[]

    for row in full_list:
        if ingredient.lower() in row:
            recipes_with_ingredient.append((f"{row[0]}, preparation time {row[1]} min"))
    return recipes_with_ingredient



        




if __name__ == "__main__":
    if True:
        found_recipes =search_by_name("recipes1.txt", "cake")
        for recipe in found_recipes:
            print(recipe)

    if True:
        found_recipes = search_by_time("recipes1.txt", 20)
        for recipe in found_recipes:
            print(recipe)
        
    if True:
        found_recipes = search_by_ingredient("recipes1.txt", "eggs")

        for recipe in found_recipes:
            print(recipe)
