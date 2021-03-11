import numpy as np 
from recipe_and_ingredient_classes import Recipe, Ingredient, KINDS


# Function to find the  
# Nth occurrence of a character  
def find_nth_occur(string, ch, N) : 
    occur = 0;  
  
    # Loop to find the Nth  
    # occurence of the character  
    for i in range(len(string)) : 
        if (string[i] == ch) : 
            occur += 1;  
  
        if (occur == N) : 
            return i;  
      
    return -1; 

def read_recipes():

    recipe_arr = []#recipes to be returned
    all_ingredient_names = []#all ingredients 

    open_file = open("cleaned_recipes.txt", 'r')#read file
    lines = open_file.readlines()#read lines
    

    for i in range(len(lines)):# go through lines

        if lines[i-1][0] == 'h':
            j = i
            ingredients_arr = []#list to hold ingredients for recipe
            
            while(lines[j] != '\n' and j < (len(lines) - 1)):
                line_split = lines[j][:-1].split()#seperate quantities from name
                ingredient_amount = line_split[0]#set quantity
                ingredient_name = " ".join(line_split[2:])#set name
                if ingredient_name not in all_ingredient_names:#if ingredient name not in total name of ingredient name
                    all_ingredient_names.append(ingredient_name)# add ingredient name
                ingredient = Ingredient(ingredient_name, float(ingredient_amount))#make new ingredient
                ingredients_arr.append(ingredient)#add ingredient to respective recipe
                j+=1

            recipe_name = lines[i-1]
            name_begin_index = find_nth_occur(recipe_name, '/', 5)
            new_recipe_name = recipe_name[name_begin_index + 1 : -2]
            final_recipe_name = new_recipe_name.replace("-", " ")
            new_recipe = Recipe(final_recipe_name, ingredients_arr)
            recipe_arr.append(new_recipe)#add recipe to list of 6 recipes

    return recipe_arr


def determine_rations(all_recipes):

    recipe_kind_ratios_added = [0,0,0,0,0,0,0,0,0,0,0]

    for recipe in all_recipes:
        ingredient_kind_amounts = [0,0,0,0,0,0,0,0,0,0,0] # this will be 11 indexes long, with the amounts of each type in the indexes respective to their position in KINDS
        for ingredient in recipe.ingredient_arr:
            ingredient_kind = ingredient.kind
            ingredient_quantity = ingredient.quantity
            kind_index = KINDS.index(ingredient_kind)
            ingredient_kind_amounts[kind_index] += ingredient_quantity
        
        recipe_kind_ratio = np.divide(ingredient_kind_amounts, sum(ingredient_kind_amounts))
        recipe_kind_ratios_added += recipe_kind_ratio

    ingredient_kind_overall_ratio = np.divide(recipe_kind_ratios_added, len(all_recipes))

    return ingredient_kind_overall_ratio

            


if __name__ == "__main__":
    all_recipes = read_recipes()

    overall_ingredient_kind_ratio = determine_rations(all_recipes)

    



