
NOVELTY_FITNESS_MULTIPLIER = 1
VALUE_FITNESS_MULTIPLIER = 1

# this function will return a fitness score based on the novelity of the recipe
def novel_fitness_function(recipe, max_num_other_ingredients):
    other_ingreients = recipe.ingredient_arr[10:]
    fitness = len(other_ingreients) / max_num_other_ingredients
    return (fitness * NOVELTY_FITNESS_MULTIPLIER)


# this function returns a fitness score based on the value of the recipe
def value_fitness_function(flavor_matrix, single_ingredients_arr, recipe):
    fitness = 0
    for ingredient in recipe.ingredient_arr:
        for i in range(len(recipe.ingredient_arr)):
            ingredient_index = single_ingredients_arr.index(ingredient.name)
            other_ingredient_index = single_ingredients_arr.index(recipe.ingredient_arr[i].name)
            fitness += flavor_matrix[ingredient_index][other_ingredient_index]
    return ((fitness / (len(recipe.ingredient_arr) - 10)) * VALUE_FITNESS_MULTIPLIER)
