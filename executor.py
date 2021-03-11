
from recipe_and_ingredient_classes import Recipe, Ingredient



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


if __name__ == "__main__":
    all_recipes = read_recipes()