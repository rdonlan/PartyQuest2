import random
from recipe_and_ingredient_classes import Recipe, Ingredient, KINDS

MAX_OUNCES = 20
RECIPE_COUNTER = 1
'''
This funtion normalizes the amount of all the ingredient to sum to 100 oz. It takes the sum of all
the ingredient quantities finds a factor to multiply each ingredient using 100/denominator. This
readjusts the sum to be 100 oz. Values are rounded to 2 decimal points. 
'''
# THIS MAY NOT BE NEEDED SINCE WE START FROM A PREDETERMINED RATIO
def normalize_recipe(recipe):
   denominator = 0 
   for ingredient in recipe.ingredient_arr:
      denominator += ingredient.quantity
   factor = 100/denominator
   for ingredient in recipe.ingredient_arr:
      #renormalize values to 2 decimal points
      ingredient.set_quantity(float("{:.2f}".format(ingredient.quantity * factor))) 


'''
Creates the first half of the next generation through recombination and mutation. Goes through the parent
generation by two's combing each set of 2 into a new offspring recipe
'''
def make_next_gen(parents, mutationRate, ingredient_kinds_array):
   #first half of next generation will be placed into next_gen
   next_gen = []
   for i in range(0, len(parents), 2):
      global RECIPE_COUNTER
      mutation = random.uniform(0,1)
      # make a new recipe list of ingredients using crossover
      new_ingredient_arr = make_offspring(parents[i], parents[i+1])
      recipe_name = new_ingredient_arr[10].name + ' cookie '
      recipe_to_add = Recipe(recipe_name + str(RECIPE_COUNTER), new_ingredient_arr)
      RECIPE_COUNTER += 1

      # If mutation value generated is less than the one set for the GA
      if (mutation < mutationRate):
         make_mutation(recipe_to_add, ingredient_kinds_array)#mutate the recipe 

      next_gen.append(recipe_to_add)

   # Normalize all recipies so they are a total of 100 oz
   # THIS MAY NOT BE NEEDED SINCE WE START FROM A PREDETERMINED RATIO
#    for recipe in next_gen:
#       normalize_recipe(recipe)
   return next_gen
      

'''
make_offsrpring preformes crossover. It finds the smaller of the two parents, generates a random number between 0 and the
len(smaller parent) which is called split index. The first cunk of the offspring list is taken from 0-splitIndex from the smaller parent.
The other chunk is taken from the split_index to the length of the larger parent created a combined child ingredient list.  
'''
def make_offspring(Parent1, Parent2):
   #if parent one is smaller
   if (len(Parent1.ingredient_arr) >= len(Parent2.ingredient_arr)):
      splitIndex = random.randint(0, len(Parent2.ingredient_arr))
      return Parent2.ingredient_arr[0:splitIndex] + Parent1.ingredient_arr[splitIndex:]
   # if parent two is smaller
   else:
      splitIndex = random.randint(0, len(Parent1.ingredient_arr)) 
      return Parent1.ingredient_arr[0:splitIndex] + Parent2.ingredient_arr[splitIndex:]
   
   
'''
make_mutation uniformly chooses between the four diffrent types of mutation possabilites. It generates a random 
number between 0 and 3 and selects mutation option based on that value. If the first mutation process is selected,
the quantity of a randomly selected ingredient is changed. If the second mutation process is selected, than a randomly 
chosen ingredient is changed to another. The third mutation adds an ingredient to the list of the ingredient for the recipe.
The final mutation process deletes a random ingredient.
'''
def make_mutation(recipe, ingredient_kinds_array):
   mutation_type = random.randint(0,4)
   # below is the index of the ingredient to change
   ingredient_to_change_index = random.randint(0, len(recipe.ingredient_arr)) - 1
   ingredient_to_change_quantity = recipe.ingredient_arr[ingredient_to_change_index].quantity
   ingredient_to_change_name = recipe.ingredient_arr[ingredient_to_change_index].name
   ingredient_to_change_kind = recipe.ingredient_arr[ingredient_to_change_index].kind
   # this below array will allow us to only swap out ingredients of the same type for when mutation_type = 1
   potential_swapable_ingredients = ingredient_kinds_array[KINDS.index(ingredient_to_change_kind)]
   
   # change the quantity of ingredient
   if(mutation_type == 0):
      new_ingredient_quantity = ingredient_to_change_quantity + float("{:.2f}".format(random.uniform(-5, 5)))
      if new_ingredient_quantity < 0:
          new_ingredient_quantity = 0.01
      new_ingredient = Ingredient(ingredient_to_change_name, new_ingredient_quantity)
      recipe.ingredient_arr[ingredient_to_change_index] = new_ingredient

   # change one ingredient to another
   elif (mutation_type == 1):
      new_ingredient_name = random.choice(potential_swapable_ingredients)
      #this while loop checks to make sure randomly selected ingredient is not already in recipe
      while(recipe.check_for_ingredient(new_ingredient_name) and len(potential_swapable_ingredients) > 1):
         #if it is, select a new name of ingredient  
         new_ingredient_name = random.choice(potential_swapable_ingredients)
      new_ingredient = Ingredient(new_ingredient_name, ingredient_to_change_quantity)
      recipe.ingredient_arr[ingredient_to_change_index] = new_ingredient
      
   # add a new ingredient
   elif(mutation_type == 2):
      new_ingredient_quantity = float("{:.2f}".format(random.uniform(2, 7)))
      new_ingredient_name = random.choice(ingredient_kinds_array[-1])
      #this while loop checks to make sure randomly selected ingredient is not already in recipe
      while(recipe.check_for_ingredient(new_ingredient_name) and len(ingredient_kinds_array[-1]) > 1): 
         #if it is, select a new name of ingredient 
         new_ingredient_name = random.choice(ingredient_kinds_array[-1])
      new_ingredient = Ingredient(new_ingredient_name, new_ingredient_quantity)
      recipe.ingredient_arr.append(new_ingredient)
      
#    # delete an ingredient from the list
#    else:
#       del recipe.ingredient_arr[ingredient_to_change_index]