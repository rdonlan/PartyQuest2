
# These are the multipliers for our value and novel fitness scores
NOVELTY_FITNESS_MULTIPLIER = 100
VALUE_FITNESS_MULTIPLIER = 100


'''
This function will return a fitness score based on the novelity of the recipe. This value is calculated as the
number of other kind ingredients in the recipe, divided by the total number of other kind ingredients, mutliplied
by its global multiplier
    Params:
        @recipe {Recipe obj}: recipe that is getting its fitness determined
        @max_num_other_ingredients {int}: the total number of unique other kind ingredients 
    Return:
        float --> the novel fitness score
'''
def novel_fitness_function(recipe, max_num_other_ingredients):
    other_ingreients = recipe.ingredient_arr[10:]
    fitness = len(other_ingreients) / max_num_other_ingredients
    return (fitness * NOVELTY_FITNESS_MULTIPLIER)


'''
This function will return a fitness score based on the value of the recipe. This value is calculated based on adding the values of 
flavor_matrix[ingredient1][ingredient2] for every pair of ingredients in the recipe's ingredient_arr. It is then divided by the number of
other kind ingredients in the recipe, and multiplied by its globalmultiplier
    Params:
        @flavor_matrix {arr[arr[float]]}: this 2D array contains N arrays that are a length of N where N is the number of unique ingredients in the
            inspiring set. Each arr will contain the correlation values for that ingredient with every other unique ingredient. The index of each ingredient in 
            @single_ingredients_arr corresponds to the index of the ingredient's correlation array within the 2D array, as well as its position in every
            other ingredient's correlation array. 
        @single_ingredients_arr corresponds to the index of the ingredient's correlation array within the 2D array, as well as its position in every
            other ingredient's correlation array. 
        @recipe {Recipe obj}: recipe that is getting its fitness determined
    Return:
        float --> the value fitness score
'''
def value_fitness_function(flavor_matrix, single_ingredients_arr, recipe):
    fitness = 0
    for ingredient in recipe.ingredient_arr:
        for i in range(len(recipe.ingredient_arr)):
            ingredient_index = single_ingredients_arr.index(ingredient.name)
            other_ingredient_index = single_ingredients_arr.index(recipe.ingredient_arr[i].name)
            fitness += flavor_matrix[ingredient_index][other_ingredient_index]
    return ((fitness / (len(recipe.ingredient_arr) - 10)) * VALUE_FITNESS_MULTIPLIER)
