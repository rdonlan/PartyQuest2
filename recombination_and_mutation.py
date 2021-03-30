import random
from recipe_and_ingredient_classes import Recipe, Ingredient, KINDS

MAX_OUNCES = 20
RECIPE_COUNTER = 1

'''
This funtion normalizes the amount of other kind ingredients to the ideal ratio based on the inspiring set. 
Values are rounded to 2 decimal points. 
   Params:
      @recipe {Recipe obj}: The recipe object that will have the quantity of its other kind ingredients normalized
      @average_recipe_ounces {float}: the average number of ounces in a recipe from our inspiring set
      @ingredient_kind_ratio_matrix {arr[float]}: contains the ratio (all add up to 1) of each kind within a recipe from the 
         inspiring set. The index of each kind correlates to its spot in the global arr from the file recipe_and_ingredient_classes.py
   Return:
      @recipe {Recipe obj}: The recipe object that has had its other kind ingredient quantities normalized
   
'''
def normalize_other_ingredients_in_recipe(recipe, average_recipe_ounces, ingredient_kind_ratio_matrix):
   average_amount_other_ingredients = average_recipe_ounces * ingredient_kind_ratio_matrix[-1]
   total_other_ingredient_ounces_in_recipe = 0
   for i in range(10, len(recipe.ingredient_arr)):
      total_other_ingredient_ounces_in_recipe += recipe.ingredient_arr[i].quantity
   # below is factor that other kind ingredients are compared to ideal ratio
   factor = total_other_ingredient_ounces_in_recipe / average_amount_other_ingredients
   # add some randomization
   factor *= random.uniform(0.9,1.1)

   # renormalizes the ingredeint amount
   for i in range(10, len(recipe.ingredient_arr)):
      recipe.ingredient_arr[i].set_quantity(float("{:.2f}".format(recipe.ingredient_arr[i].quantity / factor)))
   
   return recipe
   

'''
Creates the first half of the next generation through recombination and mutation. Goes through the parent
generation by two's combing each set of 2 into a new offspring recipe.
   Params:
      @parents {arr[Recipe objs]}: the recipes chosen for recombination from the previous generation
      @mutationRate {float}: the chance that a newly created recipe (from recombination) gets mutated
      @ingredient_kinds_array {arr[arr[str]]}: this 2D matrix holds 11 arrays which each contain the ingredients 
         of one type. So the first array contains all types of sugar from the inspiring set, the next all types
         of flour, etc.
      @average_recipe_ounces {float}: the average number of ounces in a recipe from our inspiring set
      @ingredient_kind_ratio_matrix {arr[float]}: contains the ratio (all add up to 1) of each kind within a recipe from the 
         inspiring set. The index of each kind correlates to its spot in the global arr from the file recipe_and_ingredient_classes.py
   Return:
      @next_gen {arr[Recipe objs]}: contains half of the next generation that was created from recombination and (potential) mutation
'''
def make_next_gen(parents, mutationRate, ingredient_kinds_array, average_recipe_ounces, ingredient_kind_ratio_matrix):
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

   for recipe in next_gen:
      normalize_other_ingredients_in_recipe(recipe, average_recipe_ounces, ingredient_kind_ratio_matrix)
   return next_gen
      

'''
make_offsrpring preformes crossover. It finds the smaller of the two parents, generates a random number between 0 and the
len(smaller parent) which is called split index. The first cunk of the offspring list is taken from 0-splitIndex from the smaller parent.
The other chunk is taken from the split_index to the length of the larger parent created a combined child ingredient list.  
   Params:
      @Parent1 {Recipe obj}: the first recipe parent for the recombination that will occur
      @Parent2 {Recipe obj}: the second recipe parent for the recombination that will occur
   Return:
      Recipe obj --> one of the two parent recipes with a new ingredient_arr that was created through the recombination
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
number between 0 and 2 and selects mutation option based on that value. If the first mutation process is selected,
the quantity of a randomly selected ingredient is changed. If the second mutation process is selected, than a randomly 
chosen ingredient is changed to another. The third mutation adds an ingredient to the list of the ingredient for the recipe.
There is no deletion mutation because we want to keep intact our 11 kinds, and potentially deleting an ingredient that is
the only one of its kind is not something we build our code to handle.
   Params:
      @recipe {Recipe obj}: The recipe object that will be mutated
      @ingredient_kinds_array {arr[arr[str]]}: this 2D matrix holds 11 arrays which each contain the ingredients 
         of one type. So the first array contains all types of sugar from the inspiring set, the next all types
         of flour, etc.
   Return:
      Recipe obj --> The same recipe object is returned with its ingredient_arr apporpriately changed
'''
def make_mutation(recipe, ingredient_kinds_array):
   mutation_type = random.randint(0,3)
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