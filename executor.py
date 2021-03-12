import numpy as np 
import random
from recipe_and_ingredient_classes import Recipe, Ingredient, KINDS

TOTAL_RECIPES_OUNCES = 0



# def normalize_recipe(recipe):
#    denominator = 0 
#    for ingredient in recipe.ingredient_arr:
#       denominator += ingredient.quantity
#    factor = 100/denominator
#    for ingredient in recipe.ingredient_arr:
#       #renormalize values to 2 decimal points
#       ingredient.set_quantity(float("{:.2f}".format(ingredient.quantity * factor))) 


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
    # all_ingredient_names = []#all ingredients 
    all_ingredient_matrix = [[],[],[],[],[],[],[],[],[],[],[]]

    open_file = open("cleaned_recipes.txt", 'r')#read file
    lines = open_file.readlines()#read lines
    

    for i in range(len(lines)):# go through lines

        if lines[i-1][0] == 'h':
            j = i
            ingredients_arr = []#list to hold ingredients for recipe
            
            while(lines[j] != '\n' and j < (len(lines) - 1)):
                line_split = lines[j][:-1].split()#seperate quantities from name
                ingredient_amount = line_split[0]#set quantity
                global TOTAL_RECIPES_OUNCES
                TOTAL_RECIPES_OUNCES += float(ingredient_amount)
                ingredient_name = " ".join(line_split[2:])#set name
                ingredient = Ingredient(ingredient_name, float(ingredient_amount))#make new ingredient
                if ingredient_name not in all_ingredient_matrix[KINDS.index(ingredient.kind)]:
                    all_ingredient_matrix[KINDS.index(ingredient.kind)].append(ingredient_name)
                ingredients_arr.append(ingredient)#add ingredient to respective recipe
                j+=1

            recipe_name = lines[i-1]
            name_begin_index = find_nth_occur(recipe_name, '/', 5)
            new_recipe_name = recipe_name[name_begin_index + 1 : -2]
            final_recipe_name = new_recipe_name.replace("-", " ")
            new_recipe = Recipe(final_recipe_name, ingredients_arr)
            recipe_arr.append(new_recipe)#add recipe to list of 6 recipes

    return [recipe_arr, all_ingredient_matrix]


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

            
def generate_recipes(overall_ingredient_kind_ratio, ingredient_kinds_array, num_recipes):

    generated_recipes = []

    # generating 5 new ratios
    new_ratios = []
    for i in range(5):
        cloned_ratios = overall_ingredient_kind_ratio.copy()
        for j in range(len(cloned_ratios)):
            value_to_add = np.random.uniform(-1 * cloned_ratios[j], cloned_ratios[j])
            cloned_ratios[j] = cloned_ratios[j] + value_to_add
        new_ratios.append(cloned_ratios)

    for ratio_arr in new_ratios:
        ingredient_arr = []
        for i in range(len(ingredient_kinds_array)): 
            new_ingredient_name = np.random.choice(ingredient_kinds_array[i])
            # average amount of ounces in a recipe from inspiring set times a random number for variability
            factor_to_mult_by = (TOTAL_RECIPES_OUNCES / num_recipes) * np.random.uniform(0.75, 1.5)
            new_ingredient_quantity = float("{:.2f}".format(ratio_arr[i] * factor_to_mult_by))
            ingredient_to_add = Ingredient(new_ingredient_name, new_ingredient_quantity)
            ingredient_arr.append(ingredient_to_add)
        recipe_name = ingredient_arr[-1].name + ' cookie #' + str(random.randint(0,100))
        new_recipe = Recipe(recipe_name, ingredient_arr)
        generated_recipes.append(new_recipe)

    return generated_recipes




if __name__ == "__main__":
    read_recipes_return = read_recipes()

    # list of all recipes from inspiring set
    all_recipes = read_recipes_return[0]

    # list of all ingredients sorted by their kind
    ingredient_kinds_array = read_recipes_return[1]

    # ratio (adding up to 1) or our kinds from the recipes in the inspiring set
    overall_ingredient_kind_ratio = determine_rations(all_recipes)

    new_crazy_recipes = generate_recipes(overall_ingredient_kind_ratio, ingredient_kinds_array, len(all_recipes))

    print("\n")

    for recipe in new_crazy_recipes:
        print(recipe)


    



