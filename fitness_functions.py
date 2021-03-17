
# this function will return a fitness score based on the novelity of the recipe
def novel_fitness_function(recipe):
    other_ingreients = recipe.ingredient_arr[10:]
    fitness = len(other_ingreients)
    return fitness
